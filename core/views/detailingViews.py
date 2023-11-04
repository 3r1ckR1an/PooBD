from django.views.generic import DetailView
from django.apps import apps
from ..models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Contrato, Validacao

class CategoryDetailView(DetailView):
    model = Categoria
    template_name='detail/category-detail.html'

    def get_object(self, **kwargs):
        code = self.kwargs.get("code")
        
        return self.model.objects.get(code= code)
    
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


class ContractDetailView(DetailView):
    model = Contrato
    template_name='detail/contrato-detail.html'


class PorcaoDetailView(DetailView):
    model = Porcao
    template_name='detail/porcao-detail.html'


class ValidacaoDetailView(DetailView):
    model = Validacao
    template_name='detail/validacao-detail.html'


class RestauranteDetailView(DetailView):
    model = Restaurante
    template_name='detail/restaurant-detail.html'

    def get_object(self):
        
        return self.model.objects.get(code=self.kwargs.get("code"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        restaurante = self.get_object()
        
        # Obtenha o restaurante atual
        restaurante = self.get_object()

        # Obtenha os contratos associados a este restaurante
        contratos = Contrato.objects.filter(restaurant=restaurante)
        
        print(isinstance(contratos[0].employee, Cozinheiro))
        print(isinstance(contratos[0].employee, Degustador))
        print(isinstance(contratos[0].employee, Editor))
        
        print(isinstance(contratos[1].employee, Cozinheiro))
        print(isinstance(contratos[1].employee, Degustador))
        print(isinstance(contratos[1].employee, Editor))

        cozinheiros = []
        degustadores = []
        editores = []

        for contrato in contratos:
            if isinstance(contrato.employee, Cozinheiro):
                cozinheiros.append(contrato.employee)
            elif isinstance(contrato.employee, Degustador):
                degustadores.append(contrato.employee)
            elif isinstance(contrato.employee, Editor):
                editores.append(contrato.employee)

        print(cozinheiros)
        print(degustadores)
        print(editores)
        
        context['cozinheiros'] = cozinheiros
        context['degustadores'] = degustadores
        context['editores'] = editores
        
        return context


class RecipeDetailView(DetailView):
    model = Receita
    template_name='detail/recipe-detail.html'

    def get_object(self):
        
        return self.model.objects.get(code=self.kwargs.get("code"))

