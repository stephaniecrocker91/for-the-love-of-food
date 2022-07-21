from . import views
from .views import CreateRecipeView, UpdateRecipeView
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('favourites/<slug:slug>', views.Favourite.as_view(), name='favourites'),
    path('favourites/', views.RecipeFavourites.as_view(), name='recipe_favourites'),
    path('create_recipe/', CreateRecipeView.as_view(), name='create_recipe'),
    path('create_recipe/edit/<int:pk>', UpdateRecipeView.as_view(), name='update_recipe'), 
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    # path('create_recipe/', CreateRecipeView.as_view(), name='create_recipe'),
]