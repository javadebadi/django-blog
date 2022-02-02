from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404
from blog.logic import BlogTokenize

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts':posts})

def about(request):
    return render(request, 'blog/about.html', context={})

def contact(request):
    return render(request, 'blog/contact.html', context={})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts':posts})

def post_detail(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    texts_tag = BlogTokenize(post.text).tokenize()
    return render(request, 'blog/post.html', context={'post':post, 'texts_tag':texts_tag})