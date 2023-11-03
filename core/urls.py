from django.urls import path, include
from .views import Index, CategoryListView, CheffListView, TasterListView, EditorListView, LivroListView, IngredienteListView, ReceitaListView, RestauranteListView, ContractListView, PorcaoListView, ValidationListView
from .views import CategoryDetailView, CheffDetailView, TasterDetailView, EditorDetailView, LivroDetailView, IngredienteDetailView, ReceitaDetailView, RestauranteDetailView
from .views import CategoryCreateView, UserCreateView, TasterCreateView, EditorCreateView, LivroCreateView, IngredienteCreateView, ReceitaCreateView, RestauranteCreateView, PorcaoCreateView, ContractCreateView, ValidationCreateView
from .views import CheffUpdateView, TasterUpdateView, EditorUpdateView, CategoryUpdateView, BookUpdateView, IngredientUpdateView, RestaurantUpdateView, RecipeUpdateView
from .views import ChefDeleteView, TasterDeleteView, EditorDeleteView, CategoryDeleteView, IngredientDeleteView, RecipeDeleteView, RestaurantDeleteView
from .seed import seed

# seed()

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
    path('contrato', ContractListView.as_view(), name= 'contract-list'),
    path('porcao', PorcaoListView.as_view()),
    path('validacao', ValidationListView.as_view()),
    
    path('categoria/criar', CategoryCreateView.as_view()),
    path('cozinheiro/criar', UserCreateView.as_view()),
    path('degustador/criar', TasterCreateView.as_view()),
    path('editor/criar', EditorCreateView.as_view()),
    path('livro/criar', LivroCreateView.as_view()),
    path('ingrediente/criar', IngredienteCreateView.as_view()),
    path('receita/criar', ReceitaCreateView.as_view()),
    path('restaurante/criar', RestauranteCreateView.as_view()),
    path('porcao/criar', PorcaoCreateView.as_view()),
    path('contrato/criar', ContractCreateView.as_view()),
    path('validacao/criar', ValidationCreateView.as_view()),
    
    path('cozinheiro/remover/<int:pk>', ChefDeleteView.as_view()),
    path('degustador/remover/<int:pk>', TasterDeleteView.as_view()),
    path('editor/remover/<int:pk>', EditorDeleteView.as_view()),
    path('categoria/remover/<str:code>', CategoryDeleteView.as_view()),
    path('ingrediente/remover/<str:code>', IngredientDeleteView.as_view()),
    path('receita/remover/<str:code>', RecipeDeleteView.as_view()),
    path('restaurante/remover/<str:code>', RestaurantDeleteView.as_view()),
    
    path('categoria/editar/<uuid:code>', CategoryUpdateView.as_view()),
    path('cozinheiro/editar/<str:cpf>', CheffUpdateView.as_view()),
    path('degustador/editar/<str:cpf>', TasterUpdateView.as_view()),
    path('editor/editar/<str:cpf>', EditorUpdateView.as_view()),
    path('livro/editar/<str:isbn_code>', BookUpdateView.as_view()),
    path('ingrediente/editar/<str:code>', IngredientUpdateView.as_view()),
    path('receita/editar/<str:code>', RestaurantUpdateView.as_view()),
    path('restaurante/editar/<str:code>', RecipeUpdateView.as_view()),
    
    path('categoria/<uuid:code>', CategoryDetailView.as_view(), name= "category-detail"),
    path('cozinheiro/<str:cpf>', CheffDetailView.as_view(), name= "cheff-detail"),
    path('degustador/<str:cpf>', TasterDetailView.as_view(), name= "taster-detail"),
    path('editor/<str:cpf>', EditorDetailView.as_view(), name= "editor-detail"),
    path('livro/<str:isbn_code>', LivroDetailView.as_view(), name= "livro-detail"),
    path('ingrediente/<uuid:code>', IngredienteDetailView.as_view(), name= "ingrediente-detail"),
    path('receita/<uuid:code>', ReceitaDetailView.as_view(), name= "receita-detail"),
    path('restaurante/<uuid:code>', RestauranteDetailView.as_view(), name= "restaurante-detail"),
]