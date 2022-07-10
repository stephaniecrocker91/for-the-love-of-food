from django.contrib import admin
from .models import Recipe, Categories, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    search_fields = ('title', 'content', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ['directions', 'ingredients']


admin.site.register(Categories)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'recipe', 'created_on', 'body')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
