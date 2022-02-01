from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts':posts})

def about(request):
    return render(request, 'blog/about.html', context={})

def contact(request):
    return render(request, 'blog/contact.html', context={})

def post(request):
    return render(request, 'blog/post.html', context={})