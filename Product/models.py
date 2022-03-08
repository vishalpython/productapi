import uuid
import os
from django.db import models
from User.models import User
from model_utils import Choices


def recipe_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)


class Product(models.Model):
    SIZE_CHOICES = Choices('XS', 'S', 'M', 'L', 'XL', )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=1)
    details = models.CharField(max_length=225)
    colour = models.CharField(max_length=225, null=True)
    size = models.CharField(choices=SIZE_CHOICES, max_length=225, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
