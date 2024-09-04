from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    breed = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        choices=[
            ('dog', 'Perro'),
            ('cat', 'Gato'),
        ]
    )
    status = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        choices=[
            ('adopted', 'Adoptado'),
            ('in adoption', 'En adopción'),
            ('awaiting adoption', 'En espera de adopción'),
            ('other', 'Otro'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.type})'

    class Meta:
        db_table = 'animals'
        ordering = ['created_at']
