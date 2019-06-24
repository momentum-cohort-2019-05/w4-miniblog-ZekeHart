from django.shortcuts import render
from blog.models import BlogComment, BlogPost, Author
from django.views import generic
# Create your views here.


def index(request):
    num_posts = BlogPost.objects.all().count()
    # num_users = BlogUser.objects.all().count()
    author_list = Author.objects.all()
    num_authors = Author.objects.all().count()

    context = {
        'num_posts': num_posts,
        # 'num_users': num_users,
        'author_list': author_list,
        'num_authors': num_authors
    }
    return render(request, 'index.html', context=context)


def contact(request):
    return render(request, 'contact.html', context=None)


class BlogPostDetailView(generic.DetailView):
    model = BlogPost


class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 10


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author