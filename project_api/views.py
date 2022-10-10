from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from yaml import serialize
from . import models, serializers
from rest_framework.viewsets import GenericViewSet,mixins
from datetime import date
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework import response, schemas
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from dateutil.relativedelta import relativedelta



@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='API')
    return response.Response(generator.get_schema(request=request))

class UserView(GenericViewSet, mixins.UpdateModelMixin):
    # permission_classes = [permissions.IsAuthenticated]
    queryset=models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def retrieve(self, request, pk=None):
        users = models.User.objects.filter(id= pk).first()
        loan = models.Loan.objects.filter(id=pk).first()
        print(loan)
        serializer = serializers.UserSerializer(users)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        serialize = serializers.UserSerializer(data= request.data)
        serialize.is_valid(raise_exception=True)

        return Response(serialize.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def create_account(self, request, *args, **kwargs):
        serialize = serializers.BankAccount(data= request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(serialize.data, status= status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'], url_path=r'pay/(?P<ins_id>\w+(?:-\w+)*)')
    def pay_loan(self, request, *args, **kwargs):
        user = get_object_or_404(models.User, id=kwargs['pk'])
        bank_account = get_object_or_404(models.BankAccount, user=user) 
        installment = get_object_or_404(models.Installments, id=kwargs['ins_id'])
        
        # check 
        if bank_account.balance >= installment.amount and installment.status == False:
            installment.status = True
            bank_account.balance -= installment.amount

            bank_account.save()
            installment.save()
        return Response(status= status.HTTP_201_CREATED)
class BankAccountView(GenericViewSet, mixins.UpdateModelMixin):
    queryset = models.BankAccount.objects.all()
    serializer_class = serializers.BankAccount

    def retrieve(self, request, pk=None):
        bank = models.BankAccount.objects.filter(id=pk).first()
        serializer = serializers.BankAccount(bank)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LoanView(GenericViewSet, mixins.UpdateModelMixin):
    queryset = models.Loan.objects.all()
    serializer_class = serializers.Loan

    def retrieve(self, request, pk=None):
        loan = models.Loan.objects.filter(id=pk).first()
        serializer = serializers.Loan(loan)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serialize = serializers.Loan(data= request.data)
        serialize.is_valid(raise_exception=True)
        number_of_installments = serialize.validated_data.pop('number_of_installments')
        loan = models.Loan.objects.create(**serialize.validated_data)
        arr=[]
        
        amount_to_pay = serialize.validated_data['amount']/number_of_installments
        for x in range(number_of_installments):
            arr.append(models.Installments(loan= loan, dateDue= date.today() + relativedelta(days=(x+1)*30), amount = amount_to_pay))
        models.Installments.objects.bulk_create( arr)
        return Response(status=status.HTTP_201_CREATED)


class InstallmentsView(GenericViewSet, mixins.UpdateModelMixin):
    queryset = models.Installments.objects.all()
    serializer_class = serializers.Installments

    def retrieve(self, request, pk=None):
        installments = models.Installments.objects.filter(id=pk).first()
        serializer = serializers.Installments(installments)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
