from django.contrib import admin
from .models import *


@admin.register(SalesShowroomToCustomer)
class SalesShowroomsBuyersAdmin(admin.ModelAdmin):
    readonly_fields = ("added_date",)
    list_filter = ("price", "amount_of_discount", "added_date")


@admin.register(SalesDealerToShowroom)
class SalesSuppliersShowroomsAdmin(admin.ModelAdmin):
    readonly_fields = ("added_date",)
    list_filter = ("price", "amount_of_discount", "added_date")
