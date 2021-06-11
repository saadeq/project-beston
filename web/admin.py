from django.contrib import admin
from .models import Expenses, Income

admin.site.register(Expenses)
# Register your models here.
admin.site.register(Income)
