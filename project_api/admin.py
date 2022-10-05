from django.contrib import admin

from . import models

admin.site.register(models.User)
admin.site.register(models.BankAccount)
admin.site.register(models.Installments)
admin.site.register(models.Loan)




