from get_data.utils.get_items import get_items
from django.core.management.base import BaseCommand

import environ

env = environ.Env()
environ.Env.read_env()


class Command(BaseCommand):
    def handle(self, *args, **options):
        result = get_items()

        self.stdout.write(result[1999])
