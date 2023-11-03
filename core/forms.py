from django import forms
from .models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Contrato, Validacao

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
    
    
class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'custom-class'}),
            'description': forms.TextInput(attrs={'class': 'custom-class'}),
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


class UpdateTasterForm(AddTasterForm):
    pass
    
    
class AddEditorForm(forms.ModelForm):
    class Meta(BaseUserFormMeta):
        model = Editor


class UpdateEditorForm(AddEditorForm):
    pass


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ("title", "editor")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'custom-class'}),
            'editor': forms.Select(attrs={'class': 'custom-class'}),
        }


class AddIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ("name", "description")
        widgets = {
        'name': forms.TextInput(attrs={'class': 'custom-class'}),
        'description': forms.TextInput(attrs={'class': 'custom-class'}),
    }


class UpdateIngredientForm(AddIngredientForm):
    pass


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ("name", "serving_amount", "description", "category", "chef", "book")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'custom-class'}),
            'serving_amount': forms.TextInput(attrs={'class': 'custom-class'}),
            'description': forms.TextInput(attrs={'class': 'custom-class'}),
            'category': forms.Select(attrs={'class': 'custom-class'}),
            'chef': forms.Select(attrs={'class': 'custom-class'}),
            'book': forms.Select(attrs={'class': 'custom-class'}),
        }


class UpdateRecipeForm(AddRecipeForm):
    pass


class AddRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ("name",)
        widgets = {
        'name': forms.TextInput(attrs={'class': 'custom-class'}),
    }


class UpdateRestaurantForm(AddRestaurantForm):
    pass


class CreateContractForm(forms.ModelForm):
    class Meta:
        model= Contrato
        fields = ['employee', 'restaurant']
        
        widgets = {
            'employee': forms.Select(attrs={'class': 'custom-class'}),
            'restaurant': forms.Select(attrs={'class': 'custom-class'}),
        }


class CreatePorcaoForm(forms.ModelForm):
    class Meta:
        model= Porcao
        fields = ['ingredient', 'ingredient_amount', 'measurement', 'recipe']
        
        widgets = {
            'ingredient': forms.Select(attrs={'class': 'custom-class'}),
            'ingredient_amount': forms.NumberInput(attrs={'class': 'custom-class'}),
            'measurement': forms.TextInput(attrs={'class': 'custom-class'}),
            'recipe': forms.Select(attrs={'class': 'custom-class'}),
        }


class CreateValidationForm(forms.ModelForm):
    class Meta:
        model= Validacao
        fields = ['grade', 'taster', 'recipe']
        
        widgets = {
            'grade': forms.NumberInput(attrs={'class': 'custom-class'}),
            'taster': forms.Select(attrs={'class': 'custom-class'}),
            'recipe': forms.Select(attrs={'class': 'custom-class'}),
        }
    
    def clean_grade(self):
        grade = self.cleaned_data['grade']
        if grade < 0 or grade > 5:
            raise forms.ValidationError("A nota deve estar entre 0 e 5.")
        return grade