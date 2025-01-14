from django.db import models

# Create your models here.
class Person(models.Model):
    First = models.CharField(max_length=50)
    Last = models.CharField(max_length=50)
    position = models.CharField(max_length=30)


    class Meta:
        verbose_name_plural = "Players"
