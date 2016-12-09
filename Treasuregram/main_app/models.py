from django.db import models
from django.contrib.auth.models import User

class Treasure(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='treasure_images', default='treasure_images/racerX.jpg')
    img_url = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
