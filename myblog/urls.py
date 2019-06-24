"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogposts/<int:pk>',
         views.BlogPostDetailView.as_view(),
         name='blogPost'),
    path('blogposts/', views.BlogPostListView.as_view(), name='blogposts'),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/index/', permanent=True)),
]

urlpatterns += [
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += [
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='authors'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
]