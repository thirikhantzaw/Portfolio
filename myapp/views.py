from django.shortcuts import render
from .models import TmpBannerModel,TmpTextModel
# Create your views here.


def HomePage(request):
    tmpbanner = TmpBannerModel.objects.all()
    tmptext = TmpTextModel.objects.all()
    context = {
        'tmpbanner' : tmpbanner,
        'tmptext' : tmptext
    }
    return render(request, 'index.html', context)