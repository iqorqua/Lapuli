"""
Definition of urls for Lapuli.
"""

from datetime import datetime
from django.conf.urls import url
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
    url(r'^$', app.views.home, name='home'),
]#+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)  
#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

