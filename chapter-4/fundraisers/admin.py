from django.contrib import admin

from .models import Fundraiser, Pledge, Payment

admin.site.register(Fundraiser)
admin.site.register(Pledge)
admin.site.register(Payment)
