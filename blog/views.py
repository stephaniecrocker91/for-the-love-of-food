from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm

# views here...


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginated_by = 6


class RecipeFavourites(generic.ListView):
    model = Recipe 
    template_name = 'recipe_favourites.html'
    paginated_by = 6
    context_object_name = 'recipe_favourites'  
    def get_queryset(self):
        user = self.request.user
        queryset = user.recipe_fave.all()
        return queryset

class RecipeDrafts(generic.ListView):
    model = Recipe 
    template_name = 'recipe_drafts.html'
    paginated_by = 6
    context_object_name = 'recipe_drafts'  
    def get_queryset(self):
        user = self.request.user
        queryset = Recipe.objects.filter(status=0, author=user) 
        return queryset


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = recipe.comment.order_by('created_on')
        liked = False
        faved = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        if recipe.favourites.filter(id=self.request.user.id).exists():
            faved = True

        return render(
            request, 
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comment,
                "liked": liked,
                "faved": faved,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = recipe.comment.order_by('created_on')
        liked = False
        faved = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        if recipe.favourites.filter(id=self.request.user.id).exists():
            faved = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.recipe = recipe
            comment_form.save()
        else:
            comment_form = CommentForm()

        return render(
            request, 
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comment,
                "commented": True,
                "liked": liked,
                "faved": faved,
                "comment_form": CommentForm()
            },
        )

class RecipeLike(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class Favourite(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.favourites.filter(id=request.user.id).exists():
            recipe.favourites.remove(request.user)
        else:
            recipe.favourites.add(request.user)
        
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))         


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = 'create_recipe.html'
    fields = ['title', 'category', 'author', 'ingredients', 'directions', 'image', 'status']
    # print("create recipe")
    # print(fields)
    success_url = '/'

class UpdateRecipeView(UpdateView):
    model = Recipe
    template_name = 'update_recipe.html'
    fields = ['title', 'category', 'author', 'ingredients', 'directions', 'image', 'status']
    
    print(fields)
    success_url = '/'

class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = '/'
