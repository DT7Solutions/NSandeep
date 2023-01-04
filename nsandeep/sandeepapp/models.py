from datetime import datetime
from django.db import models

# Create your models here.
class Banner(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        Description = models.CharField(max_length=100)
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title

class Portfolio(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        Description = models.CharField(max_length=100)
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title


class About(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        Description = models.CharField(max_length=2000)
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title

class BrandSlider(models.Model):
        Id = models.AutoField(primary_key=True)
        Image = models.ImageField(upload_to='uploads/')
        def __int__(self):
            return self.Id

class OurClientReview(models.Model):
        Id = models.AutoField(primary_key=True)
        Name = models.CharField(max_length=30,default="heading")
        Message = models.CharField(max_length=2000)
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Name

class Category(models.Model):
        Name = models.CharField(max_length=30,default="heading")
        Created = models.DateTimeField(default=datetime.now)
        def __str__(self):
            return self.Name
        
        class Meta:
            verbose_name ='Category'
            verbose_name_plural = 'Categories'

class BlogPost(models.Model):
    Id = models.AutoField(primary_key=True)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    Title =  models.CharField(max_length=225,default="title")
    Image1 = models.ImageField(upload_to='uploads/')
    Image2 = models.ImageField(upload_to='uploads/')
    Description1 = models.CharField(max_length=2000)
    Description2 = models.CharField(max_length=2000)
    Tags = models.CharField(max_length=100)
    CreatedName =  models.CharField(max_length=100)
    Create_at = models.DateTimeField(default=datetime.now)


    def __str__(self):
            return self.Title