from django.db import models

# Create your models here.


class City(models.Model):
    cityname = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cityname

    class Meta:
        verbose_name_plural = 'cities'
