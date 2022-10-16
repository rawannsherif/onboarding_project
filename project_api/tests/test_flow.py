from ast import Load
import json
from os import stat
from unicodedata import name
from urllib import response
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from model_bakery import baker

from project_api.serializers import GetLoanSerializer
from ..import models

class TestUserViewAPIs(APITestCase):
    
    def setUp(self):
        self.retrieveUser = '/api/user/{userId}/'
        self.payLoan = '/api/user/{userId}/pay/{ins_id}/'
        self.createUser = '/api/user/'
        self.createAccount = '/api/user/create_account/'
        self.user = baker.make(models.User, phoneNumber = "+201002495635")
        self.data = {
            'username': 'test',
            'password': 'test123',
            'email': 'test@gmail.com',
            'phoneNumber': '+201000000000'
        }
        self.account = {
            'user': self.user.id,
            'accountNumber': '123'
        }

    def tearDown(self):
        models.User.objects.all().delete()

    def test_get_user_success(self):
        response = self.client.get(self.retrieveUser.format(userId = self.user.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['id'], self.user.id)

    def test_get_user_failed(self):
        response = self.client.get(self.retrieveUser.format(userId = self.user.id +1))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_user_success(self):
        response = self.client.post(self.createUser, data = self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_user_fail(self):
        response = self.client.post(self.createUser)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_create_bankaccount_success(self):
        response = self.client.post(self.createAccount, data= self.account)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_create_bankaccount_fail(self):
        data2 = {'accountNumber': '123'}
        response = self.client.post(self.createAccount, data= data2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_pay_loan_success(self):
        loan = baker.make(models.Loan, user=self.user)
        baker.make(models.BankAccount, user=self.user)
        installment = baker.make(models.Installments, loan=loan)
        response = self.client.post(self.payLoan.format(userId = self.user.id,ins_id=installment.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_pay_loan_fail(self):
        response = self.client.post(self.payLoan.format(userId = self.user.id, ins_id=123))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class TestLoanViewAPIs(APITestCase):

    def setUp(self):
        self.retrieveLoan = '/api/loan/{loanId}/'
        self.loan = baker.make(models.Loan)

    def test_get_loan_success(self):
        response = self.client.get(self.retrieveLoan.format(loanId = self.loan.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_loan_success(self):
        







