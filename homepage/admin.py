from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from homepage.models import myuser


# https://stackoverflow.com/a/23063657
class MyUserAdmin(UserAdmin):
    model = myuser

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'homepage',)}),
    )


admin.site.register(myuser, MyUserAdmin)
