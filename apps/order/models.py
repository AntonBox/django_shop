from django.db import models
from root.base_models import TimedModel
from django.contrib.auth.models import User


class Order(TimedModel):
    user = models.ForeignKey(User)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
