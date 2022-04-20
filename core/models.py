from django.db import models

# Create your models here.

class City(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # date = models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'cities' 
