from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=50)
    red = models.IntegerField(validators=[MaxValueValidator(255)])
    green = models.IntegerField(validators=[MaxValueValidator(255)])
    blue = models.IntegerField(validators=[MaxValueValidator(255)])

