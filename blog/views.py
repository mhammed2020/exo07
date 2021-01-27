from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

# class-based view

class HomepageView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/index.html'
    context_object_name = 'posts'
