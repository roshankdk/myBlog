from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image1 = models.ImageField(upload_to="uploads/", default="uploads/dummy_image.png")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # one to many relation
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category",on_delete=models.PROTECT ,related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.TextField()  # author of the comment i.e. commenter name
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.author}" commented on blog "{self.post}"'
