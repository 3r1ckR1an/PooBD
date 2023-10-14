from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.apps import apps
from .models import Categoria

class Index(TemplateView):
    template_name='index.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        models = apps.get_models()
        my_models = [model for model in models if not model.__module__.startswith("django.")]
        models_names = [model.__name__ for model in my_models]
        
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