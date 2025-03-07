from django.db import models

# Create your models here.

from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def _str_(self):
        return f"Table {self.number} - Seats: {self.seats}"