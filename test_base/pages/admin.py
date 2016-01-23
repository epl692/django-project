from django.contrib import admin

# Register your models here.
from .models import Page
from .models import Home

admin.site.register(Home)
admin.site.register(Page)

