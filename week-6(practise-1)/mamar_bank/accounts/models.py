from django.db import models
from django.contrib.auth.models import User
from .constrants import ACCOUNT_TYPE,GENDER_TYPE


# Create your models here.

# django amader built in user make korar facility dei..

class UserBankAccount(models.Model):
    user = models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20,choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)# dui jon user er account same hobe nh.
    birth_date = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=20,choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2)

    def __str__(self) -> str:
        return str(self.account_no)


class UserAddress(models.Model):
    user = models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.user.username



class BankStatus(models.Model):
    is_bankrupt = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.is_bankrupt)