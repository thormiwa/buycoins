from django.db import models

# Create your models here.
class User(models.Model):
    user_account_number = models.CharField(max_length=255)
    user_bank_code = models.CharField(max_length=3)
    user_account_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Users'
    def __str__(self):
        return self.user_account_name