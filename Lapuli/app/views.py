"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import GoodModel
from app.models import ReviewModel
from app.localisation import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect

success = False
def home(request):
    local = rus
    """Renders the home page."""
    if 'lang' in request.COOKIES:
        value = request.COOKIES['lang']
        if value == "ua":
            local = ukr
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            messages.info(request, 'Новые отзывы!')
            form.save()
            response = HttpResponseRedirect(request.META.get('HTTP_REFERER'), locals())
            response.set_cookie('review', 'success')
            return response
    goods=GoodModel.objects.all()
    reviews = ReviewModel.objects.filter(validated=True)
    return render(request, 'app/index.html', locals())
