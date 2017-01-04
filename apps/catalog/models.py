from django.db import models
from root.base_models import TimedModel
from django.core.urlresolvers import reverse


class Category(TimedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='static/img')
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_category', kwargs={'slug': self.slug})


class Product (TimedModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='categories',)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.name
