from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.
class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    product_image = models.ImageField(upload_to='images/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'products'
        verbose_name_plural = 'products'

    def get_single_product_url(self):
        return reverse('product_details',args = [self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
