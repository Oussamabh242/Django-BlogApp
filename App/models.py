from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0, "Draft"),(1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta :
        ordering = ['-created_on']
    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            img = self.image.url
        except:
            img = ''
        return img

class Review(models.Model):
    name = models.CharField(max_length=30)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    body =models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



