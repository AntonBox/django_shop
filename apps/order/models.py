from django.db import models
from root.base_models import TimedModel


class Order(TimedModel):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
