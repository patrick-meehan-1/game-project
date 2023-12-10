from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'country', 'pin']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("country", "pin")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("country", "pin")}),)

admin.site.register(CustomUser, CustomUserAdmin)
