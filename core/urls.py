from django.urls import path, include
from .views import Index
from . import views

urlpatterns = [
    path('', Index.as_view()),
    path('cozinheiro/', views.cozinheiro, name='cozinheiro'),
]