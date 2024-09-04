from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=255,
        choices=[
            ('volunteer', 'Voluntario'),
            ('adopter', 'Adoptante'),
        ],
        default='volunteer'
    )

    def __str__(self):
        return f"{self.user.username} - {self.get_type_display()}"
    
    class Meta:
        db_table = 'user_profiles'
        ordering = ['user__username']
