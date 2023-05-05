from django.db import models

# Create your models here.
class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    imagen = models.TextField()
    visto = models.BooleanField(default=False)