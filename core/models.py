from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
from django.contrib.auth.models import User

# class user:
#     username
#     first_name
#     last_name
#     email

class PrimitiveModel():
    created_at = models.DateTimeField(auto_now_add=True)


class Categoria(models.Model, PrimitiveModel):
    code = models.IntegerField(unique=True)
    name = models.CharField()
    description = models.CharField()


class Cozinheiro(User, PrimitiveModel):
    chef_name = models.CharField(max_length=80)
    # salary = models.FloatField(max_length=8)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.IntegerField(unique=True, validators=[
            MaxLengthValidator(11),
            MinValueValidator(0),
        ])


class Degustador(User, PrimitiveModel):
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.IntegerField(unique=True, validators=[
            MaxLengthValidator(11),
            MinValueValidator(0),
        ])


class Editor(User, PrimitiveModel):
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.IntegerField(unique=True, validators=[
            MaxLengthValidator(11),
            MinValueValidator(0),
        ])


class Livro(models.Model, PrimitiveModel):
    title = models.CharField(max_length=200, unique=True)
    isbn_code = models.IntegerField(unique=True)


class Ingrediente(models.Model, PrimitiveModel):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=200, unique=True)


class Receita(models.Model, PrimitiveModel):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    chef = models.OneToOneField(Cozinheiro, on_delete=models.CASCADE)
    book = models.OneToOneField(Livro, on_delete=models.CASCADE)



class Restaurante(models.Model, PrimitiveModel):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=200, unique=True)


class IngredientInRecipe(models.Model, PrimitiveModel):
    ingredient = models.OneToOneField(Ingrediente, on_delete=models.CASCADE)
    ingredient_amount = models.IntegerField()
    measurement = models.CharField(null=True, blank=True)
    recipe = models.OneToOneField(Receita, on_delete=models.CASCADE)


class Contrato(models.Model, PrimitiveModel):
    chef = models.OneToOneField(Cozinheiro, on_delete=models.CASCADE)
    restaurant = models.OneToOneField(Restaurante, on_delete=models.CASCADE)