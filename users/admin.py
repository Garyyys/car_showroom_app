from django.contrib import admin

from users.models import ShowroomUser


@admin.register(ShowroomUser)
class ShowroomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "is_dealer",
        "is_customer",
        "is_showroom",
    )
