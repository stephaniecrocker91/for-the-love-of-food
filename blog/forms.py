from .models import Comment, Recipe
from django import forms


class CommentForm (forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('body',)

# class CreateRecipeForm(forms.ModelForm):

#     class Meta:
#         model = Recipe
#         fields = ['title', 'category', 'image', 'ingredients', 'directions']