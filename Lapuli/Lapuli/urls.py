"""
Definition of urls for Lapuli.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include 
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('app.urls')),
] \
    +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) \
    +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   
