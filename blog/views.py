from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

contents = [
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
    # return HttpResponse('<h1>About</h1>')
    return render(request, 'blog/about.html')


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date']
    template_name = 'blog/home.html'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
