import imp
from rest_framework import serializers
from . import models
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "username", "email", "phoneNumber", "password"]
        read_only_fields = ['id']
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

    def validate(self, attrs):
        if attrs.get('number_of_installments')<=0:
            raise ValidationError({'detail': 'invalid number of installments'})
        return super().validate(attrs)
