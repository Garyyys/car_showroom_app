from django.contrib import admin

from .models import Car, Dealer, DiscountDealer, LoyaltyProgram


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


@admin.register(DiscountDealer)
class DiscountDealerAdmin(admin.ModelAdmin):
    list_filter = (
        "discount",
        "bought_cars",
        "showroom",
        "dealer",
    )


@admin.register(LoyaltyProgram)
class DealerLoyaltyProgram(admin.ModelAdmin):
    readonly_fields = ("updated_at", "created_at")
    list_filter = ("dealer", "program", "min_bought_cars", "is_active")
