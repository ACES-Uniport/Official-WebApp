"""

"""
from django.contrib import admin
from django.urls import path
import AcesApp.views as views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name="home"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)