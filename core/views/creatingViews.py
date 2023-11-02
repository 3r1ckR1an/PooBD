from django.views.generic import CreateView
from django.apps import apps
from ..models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Contrato, CustomUser
from ..forms import AddCheffForm, AddTasterForm, AddEditorForm, AddBookForm, AddIngredientForm, AddRecipeForm, AddRestaurantForm, AddCategoryForm

class CategoryCreateView(CreateView):
    model = Categoria
    form_class = AddCategoryForm
    template_name='create/category-create.html'

class UserCreateView(CreateView):
    model = Cozinheiro
    form_class = AddCheffForm
    # fields = ["username", "first_name", "last_name", "email", "salary", "cpf", "chef_name"]
    template_name='create/user-create.html'


class TasterCreateView(CreateView):
    model = Degustador
    form_class = AddTasterForm
    template_name='create/user-create.html'


class EditorCreateView(CreateView):
    model = Editor
    form_class = AddEditorForm
    template_name='create/user-create.html'


class LivroCreateView(CreateView):
    model = Livro
    form_class = AddBookForm
    template_name='create/book-create.html'


class IngredienteCreateView(CreateView):
    model = Ingrediente
    form_class = AddIngredientForm
    template_name='create/ingredient-create.html'


class ReceitaCreateView(CreateView):
    model = Receita
    form_class = AddRecipeForm
    template_name='create/recipe-create.html'


class RestauranteCreateView(CreateView):
    model = Restaurante
    form_class = AddRestaurantForm
    template_name='create/restaurant-create.html'