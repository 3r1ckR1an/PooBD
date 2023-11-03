from django.views.generic import DeleteView
from ..models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Contrato, CustomUser
from django.urls import reverse_lazy

class UserDeleteBaseView(DeleteView):
    model = CustomUser
    template_name = 'delete/user_confirm_deletion.html'


class ChefDeleteView(UserDeleteBaseView, DeleteView):
    success_url = reverse_lazy('cheff-list')


class TasterDeleteView(UserDeleteBaseView):
    success_url = reverse_lazy('taster-list')


class EditorDeleteView(UserDeleteBaseView):
    success_url = reverse_lazy('editor-list')


class ObjectDeleteBaseView(DeleteView):
    template_name = 'delete/object_confirm_deletition.html'

    def get_object(self, queryset=None):
        code = self.kwargs.get('code')
        res = self.model.objects.get(code=code)
        return res


class CategoryDeleteView(ObjectDeleteBaseView):
    model = Categoria
    success_url = reverse_lazy('category-list')



class BookDeleteView(ObjectDeleteBaseView):
    model = Livro
    
    def get_object(self, queryset=None):
        isbn_code = self.kwargs.get('isbn_code')
        res = self.model.objects.get(isbn_code=isbn_code)
        return res
    success_url = reverse_lazy('book-create')


class IngredientDeleteView(ObjectDeleteBaseView):
    model = Ingrediente


class RecipeDeleteView(ObjectDeleteBaseView):
    success_url = reverse_lazy('recipe-list')


class RestaurantDeleteView(ObjectDeleteBaseView):
    model = Restaurante
    