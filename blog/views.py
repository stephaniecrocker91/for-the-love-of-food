from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginated_by = 6