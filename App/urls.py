from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<str:pk>/', views.project, name="post_detail"),
    path('about.html', views.about , name="about"),
    path('contact', views.contact , name="contact"),
]