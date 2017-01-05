from django.db import models
from root.base_models import TimedModel
from django.core.urlresolvers import reverse
from datetime import datetime


class Category(TimedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='img')
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_category', kwargs={'slug': self.slug})


class Product (TimedModel):
    def get_image_path(instance, filename):
        return 'products_img/{}/{}/{}/{}'.format(datetime.now().year,
                                                 datetime.now().month,
                                                 datetime.now().day,
                                                 filename,)

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='products',)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to=get_image_path)

    def __str__(self):
        return self.name
