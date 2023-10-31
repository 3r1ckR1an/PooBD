from django import forms
from .models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Contrato

class BaseUserFormMeta:
    fields = ("first_name", "last_name", "email", "salary", "cpf",)
    
    widgets = {
        'password': forms.PasswordInput(attrs={'class': 'custom-class'}),
        'first_name': forms.TextInput(attrs={'class': 'custom-class'}),
        'last_name': forms.TextInput(attrs={'class': 'custom-class'}),
        'email': forms.EmailInput(attrs={'class': 'custom-class'}),
        'salary': forms.NumberInput(attrs={'class': 'custom-class'}),
        'cpf': forms.TextInput(attrs={'class': 'custom-class'}),
    }
    
    
class AddCheffForm(forms.ModelForm):
    class Meta(BaseUserFormMeta):
        model = Cozinheiro
    
    
class UpdateCheffForm(forms.ModelForm):
    class Meta(BaseUserFormMeta):
        model = Cozinheiro
        
        fields = BaseUserFormMeta.fields + ('chef_name',)
        widgets = {
        'chef_name': forms.TextInput(attrs={'class': 'custom-class'}),
        **BaseUserFormMeta.widgets
    }
    
    
class AddTasterForm(forms.ModelForm):
    class Meta(BaseUserFormMeta):
        model = Degustador
    
    
class AddEditorForm(forms.ModelForm):
    class Meta(BaseUserFormMeta):
        model = Editor


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ("title", "editor")


class AddIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ("name", "description")
        widgets = {
        'name': forms.TextInput(attrs={'class': 'custom-class'}),
        'description': forms.TextInput(attrs={'class': 'custom-class'}),
    }


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ("name", "serving_amount", "description", "category", "chef", "book")


class AddRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ("name",)
        widgets = {
        'name': forms.TextInput(attrs={'class': 'custom-class'}),
    }