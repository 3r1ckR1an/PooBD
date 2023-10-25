from django import forms
from .models import Cozinheiro

class AddCheffForm(forms.ModelForm):
    class Meta:
        model = Cozinheiro
        fields = ("username", "first_name", "last_name", "email", "salary", "cpf", "chef_name")
        
        widgets = {
        'password': forms.PasswordInput(attrs={'class': 'custom-class'}),
        'username': forms.TextInput(attrs={'class': 'custom-class'}),
        'first_name': forms.TextInput(attrs={'class': 'custom-class'}),
        'last_name': forms.TextInput(attrs={'class': 'custom-class'}),
        'email': forms.EmailInput(attrs={'class': 'custom-class'}),
        'salary': forms.NumberInput(attrs={'class': 'custom-class'}),
        'cpf': forms.TextInput(attrs={'class': 'custom-class'}),
        'chef_name': forms.TextInput(attrs={'class': 'custom-class'}),
    }