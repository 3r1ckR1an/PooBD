from django.urls import path, include
from .views import Index, CategoryListView, CheffListView, TasterListView, EditorListView, LivroListView, IngredienteListView, ReceitaListView, RestauranteListView
from .views import CategoryDetailView, CheffDetailView, TasterDetailView, EditorDetailView, LivroDetailView, IngredienteDetailView, ReceitaDetailView, RestauranteDetailView
from .views import CategoryCreateView, UserCreateView, TasterCreateView, EditorCreateView, LivroCreateView, IngredienteCreateView, ReceitaCreateView, RestauranteCreateView
from .views import CheffUpdateView, TasterUpdateView, EditorUpdateView, CategoryUpdateView
from .views import ChefDeleteView
from .seed import seed

seed()

urlpatterns = [
    path('', Index.as_view()),
    
    path('categoria', CategoryListView.as_view()),
    path('cozinheiro', CheffListView.as_view(), name= "cheff-list"),
    path('degustador', TasterListView.as_view(), name= "taster-list"),
    path('editor', EditorListView.as_view(), name= "editor-list"),
    path('livro', LivroListView.as_view()),
    path('ingrediente', IngredienteListView.as_view()),
    path('receita', ReceitaListView.as_view()),
    path('restaurante', RestauranteListView.as_view()),
    
    path('categoria/criar', CategoryCreateView.as_view()),
    path('cozinheiro/criar', UserCreateView.as_view()),
    path('degustador/criar', TasterCreateView.as_view()),
    path('editor/criar', EditorCreateView.as_view()),
    path('livro/criar', LivroCreateView.as_view()),
    path('ingrediente/criar', IngredienteCreateView.as_view()),
    path('receita/criar', ReceitaCreateView.as_view()),
    path('restaurante/criar', RestauranteCreateView.as_view()),
    
    path('cozinheiro/remover/<int:pk>', ChefDeleteView.as_view()),
    
    path('categoria/editar/<uuid:code>', CategoryUpdateView.as_view()),
    path('cozinheiro/editar/<str:cpf>', CheffUpdateView.as_view()),
    path('degustador/editar/<str:cpf>', TasterUpdateView.as_view()),
    path('editor/editar/<str:cpf>', EditorUpdateView.as_view()),
    path('livro/editar/<str:cpf>', EditorUpdateView.as_view()),
    
    path('categoria/<uuid:code>', CategoryDetailView.as_view(), name= "category-detail"),
    path('cozinheiro/<str:cpf>', CheffDetailView.as_view(), name= "cheff-detail"),
    path('degustador/<str:cpf>', TasterDetailView.as_view(), name= "taster-detail"),
    path('editor/<str:cpf>', EditorDetailView.as_view(), name= "editor-detail"),
    path('livro/<str:isbn_code>', LivroDetailView.as_view(), name= "livro-detail"),
    path('ingrediente/<uuid:code>', IngredienteDetailView.as_view(), name= "ingrediente-detail"),
    path('receita/<uuid:code>', ReceitaDetailView.as_view(), name= "receita-detail"),
    path('restaurante/<uuid:code>', RestauranteDetailView.as_view(), name= "restaurante-detail"),
]