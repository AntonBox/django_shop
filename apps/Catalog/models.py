from django.db import models
from root.base_models import TimedModel

class Category(TimedModel):
    name = models.CharField(max_length = 40)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product (TimedModel):
    name = models.CharField(max_length = 30)
    category = models.ForeignKey(Category)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to= 'static/img')

    def __str__(self):
        return self.name
