from django.db import models

class Post(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=100, default=None)
    def __str__(self):
        return '{}-{}'.format(self.title,self.category)