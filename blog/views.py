from django.shortcuts import render
from blog.models import BlogsPost

def blog_index(request):
    blog_list=BlogsPost.objects.all() #获取所有数据,,获取数据库里面所拥有BlogPost对象
    return render(request,'index.html',{'blog_list':blog_list})
