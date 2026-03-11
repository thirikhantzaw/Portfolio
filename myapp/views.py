from django.shortcuts import render
from .models import TmpBannerModel
# Create your views here.


def HomePage(request):
    tmpbanner = TmpBannerModel.objects.all()
    context = {
        'tmpbanner' : tmpbanner
    }
    return render(request, 'index.html', context)