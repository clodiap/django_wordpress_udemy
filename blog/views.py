from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator

# Create your views here.
def home(request):
  post_list = Post.objects.all()
  paginator = Paginator(post_list, 2)

  return render(request, 'pages/home.html', {'posts': posts})

def single(request, single):
    single = Post.objects.get(id=single)
    context = {
        'post': single
    }
    return render(request, 'pages/single.html', context)
