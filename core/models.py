import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser

class PrimitiveModel():
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomUser(models.Model, PrimitiveModel):
    name = models.CharField(blank= True)
    email = models.EmailField(blank= True)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.CharField(max_length=11, unique=True)
    
    def __str__(self) -> str:
        return self.name


class Cozinheiro(CustomUser):
    class Meta:
        verbose_name = 'Cozinheiro'
        
    chef_name = models.CharField(max_length=80, blank=True, default='')
    
    def get_absolute_url(self):
        return reverse('cheff-detail', args=[str(self.cpf)])
    
    def __str__(self) -> str:
        return super().name


class Degustador(CustomUser):
    class Meta:
        verbose_name = 'Degustador'
        verbose_name_plural  = 'Degustadores'
    
    def get_absolute_url(self):
        return reverse('taster-detail', args=[str(self.cpf)])
    
    def __str__(self) -> str:
        return super().name


class Editor(CustomUser):
    class Meta:
        verbose_name = 'Editor'
        verbose_name_plural  = 'Editores'
    
    def get_absolute_url(self):
        return reverse('editor-detail', args=[str(self.cpf)])
    
    def __str__(self) -> str:
        return super().name


class Categoria(models.Model, PrimitiveModel):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField()
    description = models.CharField()
    
    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.code)])
    
    def __str__(self) -> str:
        return self.name


class Livro(models.Model, PrimitiveModel):
    title = models.CharField(max_length=200, unique=True)
    isbn_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('livro-detail', args=[str(self.isbn_code)])
    
    def __str__(self) -> str:
        return self.title


class Ingrediente(models.Model, PrimitiveModel):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(default='')
    
    def get_absolute_url(self):
        return reverse('ingrediente-detail', args=[str(self.code)])
    
    def __str__(self) -> str:
        return self.name


class Receita(models.Model, PrimitiveModel):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    serving_amount = models.IntegerField(default=1)
    description = models.CharField(default='', blank= True)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    chef = models.OneToOneField(Cozinheiro, on_delete=models.CASCADE)
    book = models.OneToOneField(Livro, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('receita-detail', args=[str(self.code)])
    
    def __str__(self) -> str:
        return self.name



class Restaurante(models.Model, PrimitiveModel):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200, unique=True)
    
    def get_absolute_url(self):
        return reverse('restaurante-detail', args=[str(self.code)])
    
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
    
    def get_absolute_url(self):
        return reverse('porcao-list')


class Contrato(models.Model, PrimitiveModel):
    employee = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.employee.name + '-' + self.restaurant.name
    
    def get_absolute_url(self):
        return reverse('validacao-list')


class Validacao(models.Model, PrimitiveModel):
    class Meta:
        verbose_name = 'Validação'
        verbose_name_plural = 'Validações'
    
    grade = models.IntegerField()
    taster = models.ForeignKey(Degustador, on_delete= models.CASCADE)
    recipe = models.ForeignKey(Receita, on_delete= models.CASCADE)
    
    def __str__(self) -> str:
        return self.taster.name + '-' + self.recipe.name
    
    def get_absolute_url(self):
        return reverse('validacao-detail', args=[str(self.id)])