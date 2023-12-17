from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
# always return an httpresponse or an exception



def home(request):
    context = {
        'posts': Blog.objects.all()
    }
    return render(request, 'blog/home.html', context = context)

def about(request):
    return render( request, 'blog/about.html', context = {'title': 'About'})