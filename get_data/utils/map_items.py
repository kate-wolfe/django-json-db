from datetime import datetime


def map_items(item_json):
    def barcode(varFields):
        for d in varFields:
            if d.get("fieldTag") == "b":
                barcode = d.get("content")
                return barcode

    def callnum(varFields):
        for d in varFields:
            if d.get("fieldTag") == "c":
                subList = d.get("subfields")
                for s in subList:
                    if s.get("tag") == "a":
                        callnumber = s.get("content")
                        return callnumber

    def volume(varFields):
        for d in varFields:
            if d.get("fieldTag") == "v":
                vol = d.get("content")
                return vol

    varfields = item_json["varFields"]

    def co_date():
        try:
            date = datetime.fromisoformat(item_json["fixedFields"]["63"]["value"])
            return date
        except:
            return None

    def last_co_date():
        try:
            date = datetime.fromisoformat(item_json["fixedFields"]["78"]["value"])
            return date
        except:
            return None

    def last_ci_date():
        try:
            date = datetime.fromisoformat(item_json["fixedFields"]["68"]["value"])
            return date
        except:
            return None

    new_item_schema = {
        "item_id": int(item_json["id"]),
        "barcode": barcode(varfields),
        "call_number": callnum(varfields),
        "volume": volume(varfields),
        "icode1": int(item_json["fixedFields"]["59"]["value"]),
        "icode2": item_json["fixedFields"]["60"]["value"],
        "itype_code": int(item_json["fixedFields"]["61"]["value"]),
        "location_code": item_json["fixedFields"]["79"]["value"],
        "agency_code": int(item_json["fixedFields"]["86"]["value"]),
        "item_status_code": item_json["fixedFields"]["88"]["value"],
        "item_message": item_json["fixedFields"]["97"]["value"],
        "price": float(item_json["fixedFields"]["62"]["value"]) / 100,
        "current_checkout_date": co_date(),
        "last_checkout_date": last_co_date(),
        "last_checkin_date": last_ci_date(),
        "checkout_stat_group_code": int(item_json["fixedFields"]["64"]["value"]),
        "checkin_stat_group_code": int(item_json["fixedFields"]["70"]["value"]),
        "checkout_total": int(item_json["fixedFields"]["76"]["value"]),
        "renewal_total": int(item_json["fixedFields"]["77"]["value"]),
        "last_year_to_date_checkout_total": int(
            item_json["fixedFields"]["110"]["value"]
        ),
        "year_to_date_checkout_total": int(item_json["fixedFields"]["109"]["value"]),
        "use3_count": int(item_json["fixedFields"]["74"]["value"]),
        "internal_use_count": int(item_json["fixedFields"]["93"]["value"]),
        "copy_use_count": int(item_json["fixedFields"]["94"]["value"]),
        "is_suppressed": bool(item_json["fixedFields"]["57"]["value"]),  # ?
    }

    new_record_meta = {
        "record_type_code": item_json["fixedFields"]["80"]["value"],
        "record_num": int(item_json["id"]),
        "created_date": datetime.fromisoformat(item_json["fixedFields"]["83"]["value"]),
        "updated_date": datetime.fromisoformat(item_json["fixedFields"]["84"]["value"]),
    }

    return new_item_schema, new_record_meta
