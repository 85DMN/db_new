from django.db import models
from django.utils.text import slugify

# Create your models here.
class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.CharField(max_length=90)
    release_data = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=50,unique=True)

    # def __str__(self):
    #     return self.name


