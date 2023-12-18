from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'country', 'picture', 'points']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("country", "picture", 'points')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("country", "picture", 'points')}),)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
