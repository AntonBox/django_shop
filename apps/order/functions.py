from apps.accounts.models import User
import random
import string


def create_user_order(last_name):
    username = str(last_name) + str(random.randint(1, 99))
    password = ''.join(random.choice(
        string.ascii_uppercase +
        string.ascii_lowercase + string.digits) for x in range(10))
    user = User.objects.create_user(username=username, password=password)
    return user
