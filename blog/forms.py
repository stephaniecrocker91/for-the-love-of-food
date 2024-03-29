from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title', 'category', 'ingredients', 'directions',
            'image', 'status')
        widgets = {
            'ingredients': SummernoteWidget(),
            'directions': SummernoteWidget()
        }
