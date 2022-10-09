from configparser import MAX_INTERPOLATION_DEPTH
from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length = 100, unique=True)
    email = models.EmailField(blank = True, null = True)
    phoneNumber = PhoneNumberField(unique = True)
    password = models.CharField(max_length = 100)

class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    accountNumber =  models.CharField(max_length = 100)
    balance = models.FloatField(blank = True, null = True)

class Installments(models.Model):
    numberOfInstallments = models.PositiveIntegerField()
    status = models.BooleanField(default = False)
    datedue = models.DateTimeField(auto_now_add = True, blank = True)

class Loan(models.Model):
    installments = models.OneToOneField(Installments, on_delete = models.CASCADE )
    loanAmount = models.PositiveIntegerField()
    loanStatus = models.BooleanField(default = False)


