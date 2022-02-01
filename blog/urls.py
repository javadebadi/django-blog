from django.urls import path
import blog.views as views

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('about/', views.about, name='blog_about'),
    path('post/', views.post_list, name='blog_post_list'),
    path('post/<int:pk>/', views.post_detail, name='blog_post_detail'),
    path('contact/', views.contact, name='blog_contact'),
]
