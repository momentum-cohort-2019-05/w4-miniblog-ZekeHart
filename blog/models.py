from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
# Create your models here.


class BlogPost(models.Model):
    class Meta:
        ordering = ['post_date']

    postName = models.CharField(max_length=100,
                                help_text='Enter the name of your blog post')
    postText = models.TextField(verbose_name="BlogPostText", )

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    post_date = models.DateTimeField(verbose_name="TimeOfPosting",
                                     auto_now=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('BlogPost-detail', args=[str(self.id)])


class Author(models.Model):
    """Model representing an author, a subset of BlogUser."""
    # bloguser = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,

    #     # primary_key=True,
    # )
    author_name = models.CharField(max_length=100)

    author_bio = models.TextField(verbose_name="AuthorBio",
                                  default="too boring for a bio")

    def __str__(self):
        return self.author_name


class BlogComment(models.Model):
    class Meta:
        ordering = ['comment_date']

    comment_text = models.TextField(verbose_name='Commentfield')
    blog_post = models.ForeignKey(BlogPost,
                                  on_delete=models.CASCADE,
                                  null=True)
    comment_date = models.DateTimeField(verbose_name="TimeOfPosting",
                                        auto_now=True)


# class BlogUser(models.Model):
#     user_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.user_name
