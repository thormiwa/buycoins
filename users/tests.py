import json

from graphene_django.utils.testing import GraphQLTestCase

from graphene.test import Client

from users.schema import UserType

class BuycoinsTestCase(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"

    def test_buycoins_query(self):
        print("Running test01_query_users")
        response = self.query(
            '''
            query users{
                users(userAccountNumber: "2250388835", userBankCode: "057") {
                    userBankCode
                    userAccountName
                    userAccountNumber
                }
            }
            ''',
            op_name="users"
        )
        print(response)
        content = json.loads(response.content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print(content)

    def test_buycoins_mutation(self):
        print("Running test01_query_users")
        response = self.query(
            '''
            mutation verifyUser{
                verifyUser(userAccountNumber: "2250388835", userBankCode: "057", userAccountName:"Emmanuel chukwuyem omoile") {
                    isVerified
                }
            }
            ''',
            op_name='verifyUser'
        )
        print(response)
        content = json.loads(response.content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print(content)