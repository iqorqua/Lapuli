from django.contrib import admin
from .models import *

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["reviewer_name", "validated"]
    list_filter = ['validated']
    class Meta:
        model = ReviewModel

admin.site. register(GoodModel)
admin.site. register(ReviewModel, ReviewAdmin)

