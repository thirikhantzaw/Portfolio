from django.db import models
from ckeditor.fields import RichTextField
import uuid
# Create your models here.

class TmpBannerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = RichTextField()
    position = RichTextField()
    image = models.ImageField(upload_to='TmpBanner', null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    tiktok = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name