from django.shortcuts import render
from .models import *
# Create your views here.


def HomePage(request):
    tmpbanner = TmpBannerModel.objects.order_by('-id')[:1]
    tmptext = TmpTextModel.objects.all()
    sectiontitle = SectionTitleModel.objects.all()
    companyarea = CompanyAreaModel.objects.all().order_by('id')
    tmplatestservicearea = TpmLatestServiceAreaModel.objects.all()
    textservice = TextServiceModel.objects.all()
    context = {
        'tmpbanner' : tmpbanner,
        'tmptext' : tmptext,
        'sectiontitle' : sectiontitle,
        'companyarea' : companyarea,
        'tmplatestservicearea' : tmplatestservicearea,
        'textservice' : textservice
    }
    return render(request, 'index.html', context)