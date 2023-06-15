from get_data.utils.get_items import get_items, get_item
from get_data.utils.map_items import map_items
from get_data.models import Item, RecordMetadata
from django.core.management.base import BaseCommand

import environ

env = environ.Env()
environ.Env.read_env()


class Command(BaseCommand):
    def handle(self, *args, **options):
        item_ids = get_items()

        for item in item_ids:
            item_json = get_item(item)
            item_rec, rec_meta = map_items(item_json)

            new_item = Item(**item_rec)
            new_item.save()

            new_rec = RecordMetadata(**rec_meta)
            new_rec.save()

        self.stdout.write("done")
