from django.urls import path, include
from .views import Index, CategoryListView

urlpatterns = [
    path('', Index.as_view()),
    path('categoria', CategoryListView.as_view()),
]