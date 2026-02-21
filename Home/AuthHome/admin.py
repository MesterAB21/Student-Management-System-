from django.contrib import admin

from AuthHome.models import PasswordRestRequest, CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username","email","is_staff","is_active","role","password","date_joined")
    list_filter = ("is_staff","is_active","role")
    search_fields = ("username","email")
    ordering = ("username",)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(PasswordRestRequest)

