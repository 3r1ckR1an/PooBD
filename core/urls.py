from django.urls import path, include
from .views import Index, CategoryListView, CheffListView, TasterListView, EditorListView, LivroListView, IngredienteListView, ReceitaListView, RestauranteListView, CategoryDetailView, CheffDetailView, TasterDetailView, EditorDetailView, LivroDetailView, IngredienteDetailView, ReceitaDetailView, RestauranteDetailView
from .seed import seed

seed()

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
    
    path('categoria/<uuid:code>', CategoryDetailView.as_view()),
    path('cozinheiro/<str:cpf>', CheffDetailView.as_view()),
    path('degustador/<str:cpf>', TasterDetailView.as_view()),
    path('editor/<str:cpf>', EditorDetailView.as_view()),
    path('livro/<str:isbn_code>', LivroDetailView.as_view()),
    path('ingrediente/<uuid:code>', IngredienteDetailView.as_view()),
    path('receita/<uuid:code>', ReceitaDetailView.as_view()),
    path('restaurante/<uuid:code>', RestauranteDetailView.as_view()),
]