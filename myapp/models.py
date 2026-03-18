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
    
class TmpTextModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = RichTextField()
    left_bg = models.ImageField(upload_to='TmpText/', null=True, blank=True)
    right_bg = models.ImageField(upload_to='TmpText/', null=True, blank=True)

    def __str__(self):
        return self.text
    

class SectionTitleModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = RichTextField()

    def __str__(self):
        return self.title

class CompanyAreaModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = RichTextField()
    image = models.ImageField(upload_to='CompanyArea/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class TpmLatestServiceAreaModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = RichTextField()
    title = RichTextField()
    dec = RichTextField()
    image = models.ImageField(upload_to='TpmLatestServiceArea/', null=True, blank=True)

    def __str__(self):
        return self.tag

class TextServiceModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = RichTextField()
    dec = RichTextField()

    def __str__(self):
        return self.title


