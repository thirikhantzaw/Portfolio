from django.shortcuts import render
from .models import TmpBannerModel,TmpTextModel,SectionTitleModel
# Create your views here.


def HomePage(request):
    tmpbanner = TmpBannerModel.objects.all()
    tmptext = TmpTextModel.objects.all()
    sectiontitle = SectionTitleModel.objects.all()
    context = {
        'tmpbanner' : tmpbanner,
        'tmptext' : tmptext,
        'sectiontitle' : sectiontitle
    }
    return render(request, 'index.html', context)