from django.urls import path, include
from news.views import *

urlpatterns = [
    path('echo/', echo)
]