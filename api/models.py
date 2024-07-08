from django.db import models


class Author(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(null=True)

class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="posts")
    title=models.CharField(max_length=200)
    content=models.TextField(null=True)

    