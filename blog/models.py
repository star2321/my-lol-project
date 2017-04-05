from django.db import models
from django.utils import timezone


class Post(models.Model):
    summoner = models.ForeignKey('self')
    id_key = models.CharField(max_length=200)

    def search(self):
       return self.id_key()