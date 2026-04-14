from django.db import models
# Create your models here.
from  datetime import  datetime


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

    def __repr__(self):
        return f" Pk: {self.pk}. Name: {self.name}"


class News(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(blank=True,null=True)
    published_year = models.PositiveSmallIntegerField(default=datetime.now().year)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f" Pk: {self.pk}. Name: {self.name}"

