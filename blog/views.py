from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

contents =[
    {'title': 'Blog Post 1',
    'author': 'Author 1',
    'date': '26 January 2021',
    'text': 'First blog in our project'},

     {'title': 'Blog Post 2',
    'author': 'Author 2',
    'date': '28 January 2021',
    'text': 'Second blog in our project'}
]

def about(request):
    #return HttpResponse('<h1>About</h1>')
    return render(request, 'about.html')

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'post_form.html'

