from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/index.html', context={})

def about(request):
    return render(request, 'blog/about.html', context={})

def contact(request):
    return render(request, 'blog/contact.html', context={})

def post(request):
    return render(request, 'blog/post.html', context={})