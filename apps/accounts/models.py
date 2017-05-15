from django.contrib.auth.models import AbstractUser

import itertools
import random
import string


class User(AbstractUser):
    @classmethod
    def create_user_order(cls, first_name, last_name, email):
        username = email.split('@')[0]
        extra_username = ''
        for x in itertools.count(1):
            if not User.objects.filter(username=username + extra_username).exists():
                break
            extra_username = str(x)
            username = username + extra_username
        password = ''.join(random.choice(
            string.ascii_uppercase +
            string.ascii_lowercase + string.digits) for x in range(10))
        user = cls.objects.create_user(username=username,
                                       password=password,
                                       first_name=first_name,
                                       last_name=last_name,
                                       email=email)
        return user
