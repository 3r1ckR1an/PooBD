from .listingViews import Index, CategoryListView, CheffListView, TasterListView, EditorListView, LivroListView, IngredienteListView, ReceitaListView, RestauranteListView, ContractListView

from .detailingViews import CategoryDetailView, CheffDetailView, TasterDetailView, EditorDetailView, LivroDetailView, IngredienteDetailView, ReceitaDetailView, RestauranteDetailView

from .creatingViews import CategoryCreateView, UserCreateView, TasterCreateView, EditorCreateView, LivroCreateView, IngredienteCreateView, ReceitaCreateView, RestauranteCreateView, create_contract

from .updatingViews import CheffUpdateView, TasterUpdateView, EditorUpdateView, CategoryUpdateView, BookUpdateView, IngredientUpdateView, RestaurantUpdateView, RecipeUpdateView

from .deletingViews import ChefDeleteView, TasterDeleteView, EditorDeleteView, CategoryDeleteView, IngredientDeleteView, RecipeDeleteView, RestaurantDeleteView, BookDeleteView