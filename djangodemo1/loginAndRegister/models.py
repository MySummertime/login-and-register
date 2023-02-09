
from django.db import models

# Create your models here.


# each attribute indicates a column in db
class User(models.Model):
    g = (('m', 'male'), ('f', 'female'))

    name = models.CharField('User', max_length=128, unique=True)
    password = models.CharField('Password', max_length=256)
    email = models.EmailField('Email', unique=True)
    gender = models.CharField('Gender', max_length=32, choices=g, default='m')
    create_time = models.DateTimeField('Create Time', auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-create_time']
        verbose_name = 'user'
        verbose_name_plural = 'user'


