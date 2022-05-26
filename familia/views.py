from django.http  import HttpResponse
from django.shortcuts import render

from app_familia.models import Familiar


def index(request):

    familia = Familiar.objects.all()
    
    return render(request, 'principal.html', context = {'familia': familia})