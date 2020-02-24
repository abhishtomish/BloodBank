from django.db import models

# Create your models here.

class Blood(models.Model):
    bg_group            = models.CharField(max_length = 10)
    unit_available      = models.IntegerField(default=0)

    def __str__(self):
        return self.bg_group