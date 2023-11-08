from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category_images")
    slug = models.SlugField(max_length=100, db_index=True)

    # def save(self, *args, **kwargs):
    #     # Automatically generate the slug from the name
    #     self.slug = slugify(self.name)
    #     super(Product, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"


class Product(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="product_images")
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, db_index=True)

    def save(self, *args, **kwargs):
        # Automatically generate the slug from the name
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
