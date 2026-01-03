import csv
import os
from typing import List, Dict

PURCHASE_FIELDS = [
    "category_title",
    "topup_title",
    "price_in_pence",
    "quantity",
]

def load_purchases(path: str) -> List[Dict]:
    purchases: List[Dict] = []
    if not os.path.isfile(path):
        return purchases

    try:
        with open(path, mode="r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # تطبيع بسيط للأنواع
                row["price_in_pence"] = int(row.get("price_in_pence", "0") or 0)
                row["quantity"] = int(row.get("quantity", "1") or 1)
                purchases.append(row)
    except Exception as e:
        print(f"[ERROR] Failed to load purchases: {e}")

    return purchases

def save_purchases(path: str, purchases: List[Dict]) -> None:
    try:
        with open(path, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=PURCHASE_FIELDS)
            writer.writeheader()
            writer.writerows(purchases)
    except Exception as e:
        print(f"[ERROR] Failed to save purchases: {e}")