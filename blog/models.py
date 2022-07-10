from django.db import models
# Import Django User Model and Cloudinary models.

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "DRAFT"), (1, "Published"))


# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=90)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="recipe_posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField()
    directions = models.TextField() 
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)
    favourites = models.ManyToManyField(User, related_name='recipe_fave', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
# Extra methods which can be viewed as helpers.
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_favourites(self):
        return self.favourites.count()




class Comment(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=90)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name} on {self.created_on}"







