from django.db import models
from root.base_models import TimedModel


class Carousel(TimedModel):
    img = models.ImageField(upload_to='carousel')
    title = models.CharField(max_length=120)
    index = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.title
