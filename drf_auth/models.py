from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Trip(models.Model):
    traveler = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return_string = f'{self.traveler} {self.country}'
        return return_string

    def get_absolute_url(self):
        return reverse('trip_details', args=[str(self.id)])
    
