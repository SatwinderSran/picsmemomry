from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

from django.conf import settings
from django.utils import timezone


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

class MarketingQueryset(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True).filter(start_date__lt=timezone.now()).filter(end_date__gte=timezone.now())


class MarketingManager(models.Manager):
	def get_queryset(self):
		return MarketingQueryset(self.model, using=self._db)

	def all(self):
		return self.get_queryset().active()

	def all_featured(self):
		return self.get_queryset().active().featured()

	def get_featured_item(self):
		try:
			return self.get_queryset().active().featured()[0]
		except:
			return None


class Slider(models.Model):
	image = models.ImageField(upload_to='slider_pics')	
	order = models.IntegerField(default=0)	
	header_text = models.CharField(max_length=120, null=True, blank=True)
	text = models.CharField(max_length=120, null=True, blank=True)
	active = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	start_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
	end_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

	objects = MarketingManager()

	def __str__(self):
		return str(self.image)

	class Meta:
		ordering = ['order', '-start_date', '-end_date']