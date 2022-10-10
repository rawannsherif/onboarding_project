from configparser import MAX_INTERPOLATION_DEPTH
from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    username = models.CharField(max_length = 100, unique=True)
    email = models.EmailField(blank = True, null = True)
    phoneNumber = PhoneNumberField(unique = True)
    password = models.CharField(max_length = 100)
class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    accountNumber =  models.CharField(max_length = 100)
    balance = models.FloatField(blank = True, null = True)
class Loan(models.Model):
    amount = models.PositiveIntegerField()
    status = models.BooleanField(default = False)
class Installments(models.Model):
    loan = models.ForeignKey(Loan, blank=True, null=True, on_delete = models.CASCADE)
    status = models.BooleanField(default = False)
    dateDue = models.DateTimeField(default = now)
    amount= models.PositiveIntegerField(default= True)

