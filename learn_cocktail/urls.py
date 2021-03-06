from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('question/', views.question, name='question'),
    path('answer/', views.answer, name='answer'),
    path('cocktail-list/', views.cocktail_list, name='cocktail_list'),
    path('full-cocktail-list/', views.full_cocktai_list, name='full_cocktail_list'),
]
