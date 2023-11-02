from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.apps import apps
from ..models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante

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
