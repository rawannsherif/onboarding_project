import imp
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "username", "email", "phoneNumber", "password"]

class BankAccount(serializers.ModelSerializer):
    class Meta:
        model = models.BankAccount
        fields =  [ "user", "accountNumber"]

class Installments(serializers.ModelSerializer):
    class Meta:
        model = models.Installments
        fields =  ["loan", "status", "dateDue", "amount"]

class Loan(serializers.ModelSerializer):
    number_of_installments = serializers.IntegerField()
    class Meta:
        model = models.Loan
        fields =  ["amount", "status", "number_of_installments"]

