from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    avatar = models.ImageField(blank=True, upload_to='post-images')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    def __str__(self) -> str:
        return str(self.username)


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=100)
    text = models.TextField
    image = models.TextField
    tag = models.ManyToManyField('Tag', related_name='news', blank=True)
    def __str__(self) -> str:
        return str(self.title)


class Tag(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return str(self.name)
        