from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe
from .forms import CommentForm

# Create your views here.


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginated_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = recipe.comment.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comment,
                # "commented": False, 
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = recipe.comment.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

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
                "comment_form": CommentForm()
            },
        )