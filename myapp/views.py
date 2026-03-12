from django.shortcuts import render
from .models import TmpBannerModel,TmpTextModel,SectionTitleModel,CompanyAreaModel
# Create your views here.


def HomePage(request):
    tmpbanner = TmpBannerModel.objects.all()
    tmptext = TmpTextModel.objects.all()
    sectiontitle = SectionTitleModel.objects.all()
    companyarea = CompanyAreaModel.objects.all()
    context = {
        'tmpbanner' : tmpbanner,
        'tmptext' : tmptext,
        'sectiontitle' : sectiontitle,
        'companyarea' : companyarea
    }
    return render(request, 'index.html', context)