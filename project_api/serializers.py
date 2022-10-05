import imp
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "username", "email", "phoneNumber", "password", "balance"]

class BankAccount(serializers.ModelSerializer):
    class Meta:
        model = models.BankAccount
        fields =  ["bankId", "user", "accountNumber"]

class Installments(serializers.ModelSerializer):
    class Meta:
        model = models.Installments
        fields =  ["numberOfInstallments", "status"]

class Loan(serializers.ModelSerializer):
    class Meta:
        model = models.Loan
        fields =  ["installments", "loanAmount", "loanStatus"]

