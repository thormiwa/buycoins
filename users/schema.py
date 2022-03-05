import graphene
from graphene_django import DjangoObjectType
from .models import User
from .paystack import resolve_account_name
from Levenshtein import distance as lev

class UserType(DjangoObjectType):
    class Meta: 
        model = User

class Query(graphene.ObjectType):
    users = graphene.List(UserType, user_account_number= graphene.String(required=True), user_bank_code = graphene.String())

    def resolve_users(self, info, user_account_number, user_bank_code):
        user = User.objects.filter(user_account_number=user_account_number)
        if user:
            return user
        else:
            paystack_resolution = resolve_account_name(account_number=user_account_number, bank_code=user_bank_code).capitalize()
            create_user = User.objects.create(user_account_number=user_account_number, user_bank_code=user_bank_code, user_account_name=paystack_resolution, is_verified=True)
            create_user.save()
            return User.objects.filter(user_account_number=user_account_number)

class VerifyUser(graphene.Mutation):
    class Arguments:
        # Mutation to verify a user
        user_account_number = graphene.String(required=True)
        user_bank_code = graphene.String(required=True)
        user_account_name = graphene.String(required=True)
    
    is_verified = graphene.Boolean()
    user = graphene.Field(UserType)

    @classmethod
    def mutate(self, request, info, user_account_number, user_bank_code, user_account_name):
        user = User()
        user.user_account_number = user_account_number
        user.user_bank_code = user_bank_code
        user.user_account_name = user_account_name
        is_verified = False
        if resolve_account_name(account_number=user_account_number, bank_code=user_bank_code).replace(" ", "").lower() == user_account_name.replace(" ", "").lower():
            user.save()
            return VerifyUser(user=user, is_verified=True)
        elif resolve_account_name(account_number=user_account_number, bank_code=user_bank_code).replace(" ", "").lower() != user_account_name.replace(" ", "").lower:
            paystack_result = resolve_account_name(account_number=user_account_number, bank_code=user_bank_code).replace(" ", "").lower()
            if lev(paystack_result, user_account_name.replace(" ", "").lower()) <= 2:
                user.save()
                return VerifyUser(user=user, is_verified=True)
            else:
                return VerifyUser(user=user, is_verified=False)

class Mutation(graphene.ObjectType):
    verify_user = VerifyUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)