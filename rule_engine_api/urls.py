from django.contrib import admin
from django.urls import path

from rule_engine.views import add_rule, evaluate_data

urlpatterns = [
    path('add-rule/', add_rule, name = 'add_rule'),
    path('evaluate/', evaluate_data, name = 'evaluate_data'),
]
