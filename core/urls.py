from django.urls import path, include
from .views import Index, CategoryListView, CheffListView, TasterListView, EditorListView, LivroListView, IngredienteListView, ReceitaListView, RestauranteListView

urlpatterns = [
    path('', Index.as_view()),
    path('categoria', CategoryListView.as_view()),
    path('cozinheiro', CheffListView.as_view()),
    path('degustador', TasterListView.as_view()),
    path('editor', EditorListView.as_view()),
    path('livro', LivroListView.as_view()),
    path('ingrediente', IngredienteListView.as_view()),
    path('receita', ReceitaListView.as_view()),
    path('restaurante', RestauranteListView.as_view()),
]