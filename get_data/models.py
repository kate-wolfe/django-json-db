from django.db import models


class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    barcode = models.TextField(null=True)
    call_number = models.TextField(null=True)
    volume = models.TextField(null=True)
    icode1 = models.IntegerField()
    icode2 = models.CharField(max_length=255)
    itype_code = models.IntegerField()
    location_code = models.CharField(max_length=255)
    agency_code = models.IntegerField()
    item_status_code = models.CharField(max_length=255)
    item_message = models.CharField(max_length=255)
    price = models.FloatField()
    current_checkout_date = models.DateTimeField(null=True)
    last_checkout_date = models.DateTimeField(null=True)
    last_checkin_date = models.DateTimeField(null=True)
    checkout_stat_group_code = models.IntegerField()
    checkin_stat_group_code = models.IntegerField()
    checkout_total = models.IntegerField()
    renewal_total = models.IntegerField()
    last_year_to_date_checkout_total = models.IntegerField()
    year_to_date_checkout_total = models.IntegerField()
    use3_count = models.IntegerField()
    internal_use_count = models.IntegerField()
    copy_use_count = models.IntegerField()
    is_suppressed = models.BooleanField()


class ItemJSON(models.Model):
    item_json = models.JSONField()


class RecordMetadata(models.Model):
    record_type_code = models.CharField(max_length=255)
    record_num = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
