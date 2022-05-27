from django.contrib import admin
from .models import *


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    readonly_fields = ("added_date", "date_updated",)
    list_filter = ("name", "country", "is_available",)


@admin.register(ShowroomCarForSale)
class ShowroomCarForSaleAdmin(admin.ModelAdmin):
    pass


@admin.register(DiscountShowroom)
class DiscountShowroomsAdmin(admin.ModelAdmin):
    readonly_fields = ("added_date", "date_updated",)
    list_filter = ("start_time", "end_time", "amount_of_discount", "is_available", "added_date", "date_updated",)