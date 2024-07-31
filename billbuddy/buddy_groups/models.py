from django.db import models
import uuid

class BuddyGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField('Group name', max_length=255, blank=False, null=False)
    created_date = models.DateField('Created date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Modified date', auto_now=True, auto_now_add=False)
    delete_date = models.DateField('Deleted date', auto_now=True, auto_now_add=False)


    def __str__(self):
        return f'{self.nombre}'