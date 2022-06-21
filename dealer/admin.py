from django.contrib import admin

from .models import Car, Dealer, DiscountDealer


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    readonly_fields = (
        "added_date",
        "date_updated",
        "number_of_buyers",
    )
    list_filter = (
        "name",
        "country",
        "number_of_buyers",
        "is_active",
        "added_date",
        "date_updated",
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    readonly_fields = (
        "added_date",
        "date_updated",
    )
    list_filter = (
        "make",
        "model",
        "year",
        "color",
        "engine",
        "body_type",
    )


# @admin.register(DealerCarForSale)
# class DealerCarsForSaleAdmin(admin.ModelAdmin):
#     pass


@admin.register(DiscountDealer)
class DiscountDealerAdmin(admin.ModelAdmin):
    readonly_fields = (
        "added_date",
        "date_updated",
    )
    list_filter = (
        "start_time",
        "end_time",
        "amount_of_discount",
        "is_active",
        "added_date",
        "date_updated",
    )
