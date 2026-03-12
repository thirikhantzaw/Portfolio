from django.contrib import admin
from .models import TmpBannerModel,TmpTextModel,SectionTitleModel,CompanyAreaModel
# Register your models here.

admin.site.register(TmpBannerModel)
admin.site.register(TmpTextModel)
admin.site.register(SectionTitleModel)
admin.site.register(CompanyAreaModel)