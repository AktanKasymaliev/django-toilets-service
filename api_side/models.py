from django.db import models
from user.models import User




class Entity(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=355)
    longitude = models.DecimalField(verbose_name="Долгота",max_digits=9, decimal_places=6)
    latitude = models.DecimalField(verbose_name="Широта",max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.address}"

    class Meta:
        verbose_name = 'Уборная'
        verbose_name_plural = 'Уборные'
    
class AddressImage(models.Model):
    toilet = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='toilet')
    address_image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        if self.address_image:
            return self.address_image.url
        else:
            return ''