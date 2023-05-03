from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload="categories")


class Products(BaseModel):
    category_name = models.CharField(nax_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.ImageField()
    product_description = models.TextField()


class ProductImage(BaseModel):
    product = models.ForegnKey(Product, on_delete=models.CASCADE, related_name="products_images")
    image = models.ImageField(upload="product")







