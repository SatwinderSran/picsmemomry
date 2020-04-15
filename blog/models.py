from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):    
    name = models.CharField(max_length=50) 
    city = models.CharField(max_length=50)    
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_pics')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def clean(self):
        self.name = self.name.capitalize()

    def clean(self):
        self.city = self.city.capitalize()

    
    # def save(self, *args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 1200 or img.width > 1200:
    #         output_size = (1200, 1200)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)