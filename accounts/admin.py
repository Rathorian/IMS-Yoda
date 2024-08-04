from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_active", "is_staff", "is_superuser")
    list_filter = ("is_active", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": (
            "last_name",
            "first_name",
            "email",
            "password",)}
         ),
        ("Permissions", {"fields": (
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",)}
         ),
        ("Dates importantes", {"fields": (
            "last_login",
            "date_joined",)}
         ),
    )
    add_fieldsets = (
        (None, {
            "fields": (
                "last_name",
                "first_name",
                "email",
                "password1",
                "password2",
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions"
            )
        }),
    )
    readonly_fields = ("last_login", "date_joined",)
    search_fields = ("last_name", "first_name",)
    ordering = ("last_name",)


admin.site.register(CustomUser, CustomUserAdmin)
