from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from authapp.models import CustomUser, CustomUserProfile


# Admin for CustomUser Model
class DispAdmin(CustomUserAdmin):

    # The fields to be used in displaying the User model.
    list_display = ["email", "name", "is_admin", "date_created"]
    list_filter = ["is_admin"]

    fieldsets = [
        ("credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "address", "contact_number"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]


    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["-date_created"]
    filter_horizontal = []

# Admin registration for CustomUserProfile model
class CustomUserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','otp', 'is_email_verified']


 # regestering the CustomUser model and DispAdmin in admin page
admin.site.register(CustomUser, DispAdmin)
admin.site.register(CustomUserProfile, CustomUserProfileAdmin)




