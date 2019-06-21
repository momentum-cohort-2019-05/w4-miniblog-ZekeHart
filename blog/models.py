from django.db import models

# Create your models here.


class BlogPost(models.Model):
    class Meta:
        ordering = ['post_date', 'author']

    postName = models.CharField(max_length=100,
                                help_text='Enter the name of your blog post')
    postText = models.TextField(verbose_name="BlogPostText", )

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    post_date = models.DateTimeField(verbose_name="TimeOfPosting",
                                     auto_now=True)


class Author(models.Model):
    """Model representing an author."""
    author_name = models.CharField(max_length=100)

    author_bio = models.TextField(verbose_name="AuthorBio", )

    def __str__(self):
        return self.author_name


class BlogComment(models.Model):
    class Meta:
        ordering = ['comment_date', 'author']

    comment_text = models.TextField(verbose_name='Commentfield')
    blog_post = models.ForeignKey(BlogPost,
                                  on_delete=models.CASCADE,
                                  null=True)
    comment_date = models.DateTimeField(verbose_name="TimeOfPosting",
                                        auto_now=True)
