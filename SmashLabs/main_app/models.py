from django.db import models
from django.urls import reverse

class Fighter(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    fighter_style = models.CharField(max_length=100)
    move_set = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    series_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, Series: {self.series_name}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'fighter_id': self.id})

class Stage(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    series_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, Series: {self.series_name}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'stage_id': self.id})
