from django.contrib import admin
from blog.models import BlogsPost

class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title','body','timestamp']
admin.site.register(BlogsPost,BlogsPostAdmin) #将两个类添加到后台管理