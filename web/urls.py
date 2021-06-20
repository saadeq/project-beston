from django.urls import path

from . import views

urlpatterns=[
    path('submit/expenses/', views.submit_expenses, name='submit_expenses'),
]