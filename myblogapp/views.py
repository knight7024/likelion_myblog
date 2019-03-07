from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.

def index(request):
    blogs = Blog.objects
    return render(request, 'myblogapp/index.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'myblogapp/detail.html', {'blog': blog_detail})

def create_post(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.author = request.user.get_username()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def create(request):
    return render(request, 'myblogapp/create.html')