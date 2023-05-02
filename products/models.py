from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_name = models.ImageField(upload="categories")


class Products(BaseModel):
    category_name = models.CharField(nax_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASED, related_name="products")
    price = models.ImageField()
    product_description = models.TextField()


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    product_description = models.TextField()


class ProductImage(BaseModel):
    product = models.ForegnKey(Product, on_delete=models.CASCADE, related_name="products_images")
    image = models.ImageField(upload="product")







