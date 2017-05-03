from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")
