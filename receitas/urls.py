from django import urls
from django.urls import include, path

from . import views
import receitas

urlpatterns = [
    path('', views.index, name='index'),
    path('receita', views.receita, name='receita')
]