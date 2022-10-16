from email.mime import base
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from project_api import views

from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema


schema_view = get_schema_view(openapi.Info(title="External Account Service API",
                                           default_version='v1',
                                           description="API Endpoints for OCTO EAS Service",
                                           terms_of_service="https://www.getocto.io/",
                                           contact=openapi.Contact(name="Octo",
                                                                   email="info@Octo.com",
                                                                   url="info@Octo.com"),
                                           license=openapi.License(
                                               name="Octo License", url="info@octo.com"),
                                           ),
                              generator_class=BothHttpAndHttpsSchemaGenerator,
                              public=True,
                              permission_classes=(permissions.AllowAny,),
                              )


router = DefaultRouter()
router.register('user', views.UserView, basename='users-urls')
router.register('bank', views.BankAccountView, basename='bank-urls')
router.register('loan', views.LoanView, basename='loan-urls')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^$', views.schema_view),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
