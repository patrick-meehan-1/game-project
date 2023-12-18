from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Game, Season

# Register your models here.
admin.site.register(Game)
admin.site.register(Season)
