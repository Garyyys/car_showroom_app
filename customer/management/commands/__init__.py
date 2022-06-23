from django.core.management.base import BaseCommand
from core.database_auto_fill_tools.customers_auto_fill import fill_db


class Command(BaseCommand):
    help = "This command generate and filling random customers i db"

    def handle(self, *args, **options):
        fill_db()
