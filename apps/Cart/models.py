from django.db import models
from root.base_models import TimedModel
from apps.Catalog.models import Product


class CartItem(TimedModel):
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()

class User(TimedModel):
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    password = models.CharField(max_length = 25)

    def __str__(self):
        return self.name

class Cart(TimedModel):
    OPEN = 'Open'
    CLOSED = 'Closed'
    status_choice = ( (OPEN, 'Open'), (CLOSED, 'Closed') )
    user = models.ForeignKey('User')
    status = models.CharField(max_length = 6, choices = status_choice, default = 'Closed')

    def __str__(self):
        return self.status
