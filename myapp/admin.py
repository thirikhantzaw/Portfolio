from django.contrib import admin
from .models import TmpBannerModel,TmpTextModel,SectionTitleModel,CompanyAreaModel,TpmLatestServiceAreaModel,TextServiceModel
# Register your models here.

admin.site.register(TmpBannerModel)
admin.site.register(TmpTextModel)
admin.site.register(SectionTitleModel)
admin.site.register(CompanyAreaModel)
admin.site.register(TpmLatestServiceAreaModel)
admin.site.register(TextServiceModel)