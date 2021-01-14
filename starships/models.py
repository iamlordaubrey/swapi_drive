from django.db import models


class Starship(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=300)
    crew = models.CharField(max_length=255, blank=True)
    passengers = models.CharField(max_length=50, blank=True)
    cargo_capacity = models.PositiveBigIntegerField(blank=True)
    consumables = models.CharField(max_length=100)
    hyperdrive_rating = models.DecimalField(max_digits=3, decimal_places=1)
    starship_class = models.CharField(max_length=100)
    url = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
