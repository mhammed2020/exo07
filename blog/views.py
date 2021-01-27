from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

# class-based view

class HomepageView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    
    
from django.core.paginator import Paginator

def function_based(request):

    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,
                  'blog/function_based.html',
                  {'posts': posts})