from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.apps import apps
from .models import Categoria, Cozinheiro

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
            try:
                name = model._meta.verbose_name
            except AttributeError:
                name = model.__name__
            
            print(name)
            
            models_names.append(name)

        context = super().get_context_data(**kwargs)
        context['models'] = models_names
        
        return context


class CategoryListView(ListView):
    model = Categoria
    template_name='category-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorias = Categoria.objects.all()
        print(categorias)
        context['categorias'] = categorias
        
        return context


class CheffListView(ListView):
    model = Cozinheiro
    template_name='cheff-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cheffs = Cozinheiro.objects.all()
        print(cheffs)
        context['cheffs'] = cheffs
        
        return context