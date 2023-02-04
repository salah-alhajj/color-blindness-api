from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include


def index(request):
    return render(request, 'index.html')


urlpatterns = [
                  path('', index),
                  path('api/process', include('Proccesser.urls')),
                  path('api/process/', include('Proccesser.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
