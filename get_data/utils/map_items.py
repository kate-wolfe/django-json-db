"""
# id must be string, not integer

result = session.get(get_items_url, params=get_items_params)

item_json = result.json()

new_schema = {"item_id": item_json["id"], "barcode": "test"}

new_item = ItemJSON()
new_item.item_json = new_schema
new_item.save()
"""
