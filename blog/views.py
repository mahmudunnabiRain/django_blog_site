from django.shortcuts import render
from django.http import HttpResponse

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

def home(request):
    context = {
        'posts': contents,
        'title': 'HomePage'
    }
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse('<h1>About</h1>')
    context = {
        'title': 'About'
    }
    return render(request, 'about.html', context)
