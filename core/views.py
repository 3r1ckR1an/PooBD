from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name='index.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        return context
    
def cozinheiro(request):
    return render(request, 'cozinheiro.html')