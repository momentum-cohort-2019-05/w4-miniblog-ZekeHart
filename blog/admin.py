from django.contrib import admin
from blog.models import BlogComment, BlogPost, Author
# Register your models here.

admin.site.register(BlogComment)
admin.site.register(Author)
admin.site.register(BlogPost)