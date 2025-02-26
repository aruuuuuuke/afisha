import random
from django.db import models
from django.contrib.auth.models import User

class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    is_confirmed = models.BooleanField(default=False)

    def generate_code(self):
        self.code = str(random.randint(100000, 999999))
        self.save()

    def __str__(self):
        return f'Code for {self.user.username}'
