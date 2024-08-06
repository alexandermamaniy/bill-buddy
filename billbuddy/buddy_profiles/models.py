from django.db import models
import uuid
from users.models import User

def upload_to(instance, filename):
    return f'images/{filename}'

class BuddyProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Buddy Profile')
    full_name = models.CharField('Fullname', max_length=255, blank=True, null=False)
    picture_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_date = models.DateField('Created date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Modified date', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Deleted date', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Buddy Profile'
        verbose_name_plural = 'Buddy Profiles'
        ordering = ['full_name']

    def __str__(self):
        return f'{self.full_name}'