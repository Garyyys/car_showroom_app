from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ("added_date", "date_updated",)
    list_filter = ("name", "age", "sex", "country", "added_date", "date_updated",)


@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    readonly_fields = ("added_date", "date_updated",)
    list_filter = ("price", "added_date", "date_updated",)
