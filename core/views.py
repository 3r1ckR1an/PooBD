from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView, UpdateView, DeleteView
from django.apps import apps
from .models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Contrato, CustomUser
from .forms import AddCheffForm, AddTasterForm, AddEditorForm, AddBookForm, AddIngredientForm, AddRecipeForm, AddRestaurantForm, UpdateCheffForm
from django.urls import reverse_lazy

class Index(TemplateView):
    template_name='index.html'
    
    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     models = apps.get_models()
    #     my_models = [model for model in models if not model.__module__.startswith("django.")]
    #     models_names = [model.__name__ for model in my_models]
        
    #     context = super().get_context_data(**kwargs)
    #     context['models'] = models_names
        
    #     print(models_names)
        
    #     return context
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        models = apps.get_models()
        my_models = [model for model in models if not model.__module__.startswith("django.")]
        models_names = []
        
        for model in my_models:
            if model.__name__ not in ["Porcao", "Contrato", "Validacao", "Composicao", "CustomUser"]:
                try:
                    name = model._meta.verbose_name
                except AttributeError:
                    name = model.__name__
                
                models_names.append(name)

        context = super().get_context_data(**kwargs)
        context['models'] = models_names
        
        return context


class CategoryListView(ListView):
    model = Categoria
    template_name='list/category-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorias = self.model.objects.all()
        print(categorias)
        context['categorias'] = categorias
        
        return context


class CheffListView(ListView):
    model = Cozinheiro
    template_name='list/cheff-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cheffs = self.model.objects.all()
        print(cheffs)
        context['cheffs'] = cheffs
        
        return context


class TasterListView(ListView):
    model = Degustador
    template_name='list/taster-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class EditorListView(ListView):
    model = Editor
    template_name='list/editor-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class LivroListView(ListView):
    model = Livro
    template_name='list/book-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class IngredienteListView(ListView):
    model = Ingrediente
    template_name='list/ingredient-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class ReceitaListView(ListView):
    model = Receita
    template_name='list/recipe-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class RestauranteListView(ListView):
    model = Restaurante
    template_name='list/restaurant-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

#==============================================================

class CategoryDetailView(DetailView):
    model = Categoria
    template_name='detail/category-detail.html'

    def get_object(self, **kwargs):
        
        return self.model.objects.get(code=self.kwargs.get("code"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        category = self.get_object()
        context['recipes']= Receita.objects.filter(category__code= category.code)
        
        return context


class CheffDetailView(DetailView):
    model = Cozinheiro
    template_name='detail/cheff-detail.html'

    def get_object(self):
        
        return self.model.objects.get(cpf=self.kwargs.get("cpf"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        chef = self.get_object()
        context['recipes'] = Receita.objects.filter(chef__cpf= chef.cpf)
        
        return context


class TasterDetailView(DetailView):
    model = Degustador
    template_name='detail/taster-detail.html'

    def get_object(self):
        
        return self.model.objects.get(cpf=self.kwargs.get("cpf"))


class EditorDetailView(DetailView):
    model = Editor
    template_name='detail/editor-detail.html'

    def get_object(self):
        
        return self.model.objects.get(cpf=self.kwargs.get("cpf"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        editor = self.get_object()
        context['books'] = Livro.objects.filter(editor__cpf= editor.cpf)
        
        return context


class LivroDetailView(DetailView):
    model = Livro
    template_name='detail/book-detail.html'

    def get_object(self):
        
        return self.model.objects.get(isbn_code=self.kwargs.get("isbn_code"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        book = self.get_object()
        context['recipes']= Receita.objects.filter(book__title= book.title)
        
        return context


class IngredienteDetailView(DetailView):
    model = Ingrediente
    template_name='detail/ingredient-detail.html'

    def get_object(self):
        
        return self.model.objects.get(code=self.kwargs.get("code"))


class ReceitaDetailView(DetailView):
    model = Receita
    template_name='detail/recipe-detail.html'

    def get_object(self):
        
        return self.model.objects.get(code=self.kwargs.get("code"))


class RestauranteDetailView(DetailView):
    model = Restaurante
    template_name='detail/restaurant-detail.html'

    def get_object(self):
        
        return self.model.objects.get(code=self.kwargs.get("code"))


#==============================================================
class CategoryCreateView(CreateView):
    model = Categoria
    fields = ["name", "description"]
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
    template_name='create/user-create.html'


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


#==============================================================
class CheffUpdateView(UpdateView):
    model = Cozinheiro
    form_class = UpdateCheffForm
    template_name='create/restaurant-create.html'
    
    def get_object(self, queryset=None):
        cpf = self.kwargs.get('cpf')
        return self.model.objects.get(cpf=cpf)


#==============================================================
class UserDeleteBaseView:
    model = CustomUser
    template_name = 'delete/confirm_deletion.html'


class ChefDeleteView(UserDeleteBaseView, DeleteView):
    success_url = reverse_lazy('cheff-list')


class TasterDeleteView(DeleteView, UserDeleteBaseView):
    success_url = reverse_lazy('/degustador')


class EditorDeleteView(DeleteView, UserDeleteBaseView):
    success_url = reverse_lazy('/editor')