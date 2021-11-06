from django.contrib import admin
from .models import Post, Review

# Register your models here..

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'post','created_on')
    search_fields = ['name', 'body']

admin.site.register(Post, PostAdmin)
admin.site.register(Review, ReviewAdmin)