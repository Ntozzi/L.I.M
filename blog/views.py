from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def all_blogs(request):
    text = Blog.objects.all().order_by('-date')[:5]
    return render(request,'Blog/all_blogs.html',{'text': text})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) # pk stands for primary key, we are looping through all id and if exist we reflect it.
    return render(request, 'Blog/detail.html', {'blog':blog})


