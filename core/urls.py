from django.urls import path, include
from .views import Index, CategoryListView, CheffListView

urlpatterns = [
    path('', Index.as_view()),
    path('categoria', CategoryListView.as_view()),
    path('cozinheiro', CheffListView.as_view()),
    # path('degustador', CheffListView.as_view()),
    # path('editor', CheffListView.as_view()),
    # path('livro', CheffListView.as_view()),
    # path('ingrediente', CheffListView.as_view()),
    # path('receita', CheffListView.as_view()),
    # path('restaurante', CheffListView.as_view()),
    # path('porcao', CheffListView.as_view()),
    # path('contrato', CheffListView.as_view()),
]