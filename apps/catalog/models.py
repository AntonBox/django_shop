from django.db import models
from root.base_models import TimedModel
from django.db.models import permalink


class Category(TimedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('view_category_url', None, {'slug': self.slug})


class Product (TimedModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='static/img')

    def __unicode__(self):
        return self.name
