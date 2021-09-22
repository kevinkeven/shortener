from django.db import models
import string
import uuid
import random

from django.urls import reverse

def get_random_string():
    length = 7
    letters = string.ascii_letters + string.digits
    result = ''.join(random.choice(letters) for i in range(length))
    return result

# Create your models here.
class SHORTURL(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url_path = models.URLField(max_length=120, blank=True)
    orignalurl = models.CharField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self, *args, **kwargs):
        return reverse("yeah", args=[self.id])


    def __str__(self):
        return self.url_path