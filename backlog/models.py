from django.db import models

# Create your models here.
class games(models.Model):
    Playstation = 'PS'
    Xbox = 'XB'
    CONSOLE_CHOICES = [
        (Playstation, 'Playstation'),
        (Xbox, 'Xbox'),
    ]

    title   = models.CharField(max_length=100)
    genre   = models.CharField(max_length=100)
    console = models.CharField(
        max_length=2,
        choices=CONSOLE_CHOICES,
        default=Xbox
    )
    started = models.BooleanField()
    
    def __str__(self):
        return self.title
    