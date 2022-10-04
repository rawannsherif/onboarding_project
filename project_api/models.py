from configparser import MAX_INTERPOLATION_DEPTH
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    id = models.CharField(primary_key = True, max_length = 256)
    username = models.CharField(max_length = 100)
    email = models.EmailField(blank = True, null = True)
    phoneNumber = PhoneNumberField(unique = True)
    password = models.CharField(max_length = 100)
    balance = models.FloatField()

    def __str__(self):
        return self.task

class BankAccount(models.Model):
    bankId = models.CharField(primary_key = True, max_length = 256)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    accountNumber =  models.CharField(max_length = 100)

class Installments(models.Model):
    numberOfInstallments = models.PositiveIntegerField()
    status = models.BooleanField(default = False)

class Loan(models.Model):
    installments = models.OneToOneField(Installments, on_delete = models.CASCADE )
    loanAmount = models.PositiveIntegerField()
    loanStatus = models.BooleanField(default = False)


