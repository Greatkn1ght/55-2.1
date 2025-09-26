from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

User = settings.AUTH_USER_MODEL

class ConfirmationCode(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='confirmation_code'
    )

    code = models.CharField(max_length = 6)

    def __str__(self):
        return f"{self.user} - {self.code}"