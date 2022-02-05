from django.shortcuts import render
from blog.models import (
    Post,
    ContactMessage,
)
from django.shortcuts import get_object_or_404
from blog.logic import BlogTokenize
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import ContactMessageForm


# Create your views here.
def home(request):
    posts = Post.objects.all()[:2]
    return render(request, 'blog/index.html', context={'posts':posts})

def about(request):
    return render(request, 'blog/about.html', context={})

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            print(" =============== Clean Data =================")
            print(form.cleaned_data)
            ContactMessage.objects.create(
                name=form.cleaned_data.get("name"),    
                email=form.cleaned_data.get("email"),    
                message=form.cleaned_data.get("message"),    
                phone_number=form.cleaned_data.get("phone_number"),    
            )
        return render(request, 'blog/thanks.html', context={})
    if request.method == 'GET':
        form = ContactMessageForm()
        return render(request, 'blog/contact.html', context={'form': form})

def post_list(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get("page")
    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        page = paginator.page(1)
    posts = page.object_list
    context = {
        'posts': posts,
        'page': page,
    }
    return render(request, 'blog/post_list.html', context=context)

def post_detail(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    texts_tag = BlogTokenize(post.text).tokenize()
    return render(request, 'blog/post.html', context={'post':post, 'texts_tag':texts_tag})