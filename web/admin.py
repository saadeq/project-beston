from django.contrib import admin
from .models import Expenses, Income, Token

admin.site.register(Expenses)
# Register your models here.
admin.site.register(Income)

admin.site.register(Token)

