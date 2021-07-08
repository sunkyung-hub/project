from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone 
from .models import Blog 
# Create your views here.

def home(request):
    blogs  = Blog.objects.all()
    #변수    #models의 Blog 
    return render(request, 'home.html', {'blogs':blogs})
                                         #앞 blog - home에서 사용하는 blog
def detail(request, id):
    blog = get_object_or_404(Blog, pk = id) #pk=primary key, 데이터 베이스에서 데이터들을 식별하기 위한 키
    return render(request, 'detail.html', {'blog':blog.id})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now() 
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id= id)
    return render(request, 'edit.html', {'blog':edit_blog})
    
def update(request, id):
    update_blog = Blog.objects.get(id = id)
    update_blog = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now() 
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')
