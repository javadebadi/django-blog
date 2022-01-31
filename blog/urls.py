from django.urls import path
import blog.views as views

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('about/', views.about, name='blog_about'),
    path('post/', views.post, name='blog_post'),
    path('contact/', views.contact, name='blog_contact'),
]
