from django.db import models

# Create your models here.


from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


class Pokemon(models.Model):
    
    name = models.CharField(max_length=50, primary_key=True)
    base_experience = models.IntegerField(default=0)

    image_url = models.URLField(blank=True)
