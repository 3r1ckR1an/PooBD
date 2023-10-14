import uuid
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
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField()
    description = models.CharField()
    
    def __str__(self) -> str:
        return self.name


class Cozinheiro(User, PrimitiveModel):
    class Meta:
        verbose_name = 'Cozinheiro'
        
    chef_name = models.CharField(max_length=80, blank=True, default='')
    # salary = models.FloatField(max_length=8)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.CharField(max_length=11, unique=True)
    
    def __str__(self) -> str:
        return super().first_name


class Degustador(User, PrimitiveModel):
    class Meta:
        verbose_name = 'Degustador'
        verbose_name_plural  = 'Degustadores'
        
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.CharField(max_length=11, unique=True)
    
    def __str__(self) -> str:
        return super().first_name


class Editor(User, PrimitiveModel):
    class Meta:
        verbose_name = 'Editor'
        verbose_name_plural  = 'Editores'
        
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.CharField(max_length=11, unique=True)
    
    def __str__(self) -> str:
        return super().first_name


class Livro(models.Model, PrimitiveModel):
    title = models.CharField(max_length=200, unique=True)
    isbn_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self) -> str:
        return self.title


class Ingrediente(models.Model, PrimitiveModel):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self) -> str:
        return self.name


class Receita(models.Model, PrimitiveModel):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    chef = models.OneToOneField(Cozinheiro, on_delete=models.CASCADE)
    book = models.OneToOneField(Livro, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name



class Restaurante(models.Model, PrimitiveModel):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self) -> str:
        return self.name


class Porcao(models.Model, PrimitiveModel):
    class Meta:
        verbose_name = 'Porção'
        verbose_name_plural = 'Porções'
        
    ingredient = models.OneToOneField(Ingrediente, on_delete=models.CASCADE)
    ingredient_amount = models.IntegerField()
    measurement = models.CharField(null=True, blank=True)
    recipe = models.OneToOneField(Receita, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.ingredient.name + '-' + self.recipe.name


class Contrato(models.Model, PrimitiveModel):
    chef = models.OneToOneField(Cozinheiro, on_delete=models.CASCADE)
    restaurant = models.OneToOneField(Restaurante, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.chef.first_name + '-' + self.restaurant.name