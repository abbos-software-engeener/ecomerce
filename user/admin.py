from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.forms import UserChangeForm



class UserAdmin(UserAdmin):
    model = User
    list_display = ('phone', 'is_staff', 'is_active')
    list_filter = ('phone', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields':('phone', 'password')}),
        ("Permissions", {'fields':('is_staff', "is_active")})
    )
admin.site.register(User)