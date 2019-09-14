from django.db import models

class people(models.Model):
    username = models.CharField(max_length=10)
    mob_no = models.CharField(max_length=10)
    odr_id = models.IntegerField()

    def __str__(self):
        return self.username
