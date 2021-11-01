
from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(blank=True)
    cat_image=models.ImageField(upload_to='photos/categories',blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('products_by_category',args=[self.slug])
    def __str__(self):
        return self.category_name