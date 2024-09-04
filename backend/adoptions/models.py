from django.db import models
from django.contrib.auth.models import User
from animals.models import Animal

class Adoption(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adopter = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('completed', 'Completado'),
        ('in process', 'En proceso'),
        ('other', 'Otro')
    ], default='completed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.adopter.username} adopted {self.animal.name} on {self.date}'

    class Meta:
        db_table = 'adoptions'
        ordering = ['-date']
