from django.contrib.auth.models import Permission, User
from django.db import models
#from camera_network import *

#camera = CameraNetwork()

class Operater(models.Model):
    kreirao = models.ForeignKey(User, default=1) # tko je izradio
    nalog = models.CharField(max_length=500) # ime naloga
    sifra = models.CharField(max_length=500)
    slika = models.FileField() # ako treba dodaj sliku
    is_star = models.BooleanField(default=False) # oznaci prioritetom

    def __unicode__(self):
        return self.nalog + ' - ' + self.sifra

class Pwm(models.Model):
    period = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sirina = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
