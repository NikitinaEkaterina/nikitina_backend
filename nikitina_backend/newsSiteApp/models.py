from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    avatar = models.TextField
    def __str__(self) -> str:
        return str(self.username)

class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    tittle = models.CharField(max_length=100)
    text = models.TextField
    image = models.TextField
    tag = models.ManyToManyField('Tag', related_name='news', blank=True)
    def __str__(self) -> str:
        return str(self.tittle)

class Tag(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return str(self.name)