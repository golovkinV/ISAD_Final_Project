from django.shortcuts import render
from news.models import *


# Create your views here.
def echo(request):
    print(News.objects.all())
    return render(request, 'echo.html')
