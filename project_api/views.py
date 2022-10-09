from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from rest_framework.viewsets import GenericViewSet,mixins

from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Bookings API')
    return response.Response(generator.get_schema(request=request))

class UserView(GenericViewSet, mixins.UpdateModelMixin):
    # permission_classes = [permissions.IsAuthenticated]
    queryset=models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def retrieve(self, request, pk=None):
        users = models.User.objects.filter(id= pk).first()
        serializer = serializers.UserSerializer(users)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serialize = serializers.UserSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)

        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class BankAccountView(GenericViewSet, mixins.UpdateModelMixin):
    queryset = models.BankAccount.objects.all()
    serializer_class = serializers.BankAccount

    def retrieve(self, request, pk=None):
        bank = models.BankAccount.objects.filter(id= pk).first()
