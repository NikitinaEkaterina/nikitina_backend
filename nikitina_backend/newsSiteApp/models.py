from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to='post-images')
    email = models.EmailField(blank=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self) -> str:
        return self.username

class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images')
    tag = models.ManyToManyField('Tag', related_name='news', blank=True)

    def __str__(self) -> str:
        return str(self.title)


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return str(self.name)

