from django.urls import path
import blog.views as views

urlpatterns = [
    path('', views.home, name='blog_home'),
]
