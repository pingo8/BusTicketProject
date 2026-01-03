import csv
from typing import List, Tuple
from models import Category, TopUp

REQUIRED_COLUMNS = set()  # سنملأها بعد ما ترسل header

def load_data(csv_path: str) -> Tuple[List[Category], List[TopUp]]:
    categories: List[Category] = []
    topups: List[TopUp] = []
    seen_categories = set()

    try:
        with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)

            if not reader.fieldnames:
                raise ValueError("CSV has no header row.")

            if REQUIRED_COLUMNS:
                missing = REQUIRED_COLUMNS - set(reader.fieldnames)
                if missing:
                    raise ValueError(f"Missing columns: {sorted(missing)}")

            for row in reader:
                cat_title = row["category_title"].strip()
                cat_desc = row["category_description"].strip()

                if cat_title not in seen_categories:
                    categories.append(Category(title=cat_title, description=cat_desc))
                    seen_categories.add(cat_title)

                price = int(row["topup_price_in_pence"].strip())

                topups.append(
                    TopUp(
                        category_title=cat_title,
                        title=row["topup_title"].strip(),
                        description=row["topup_description"].strip(),
                        price_in_pence=price,
                        entitlement_type=row["topup_entitlement_type"].strip(),
                        entitlement_unit=row["topup_entitlement_unit"].strip(),
                        entitlement_value=row["topup_entitlement_value"].strip(),
                        entitlement_quantity=row["topup_entitlement_quantity"].strip(),
                        passenger_class_name=row["topup_passenger_class_name"].strip(),
                        passenger_class_quantity=row["topup_passenger_class_quantity"].strip(),
                    )
                )

    except FileNotFoundError:
        print(f"[ERROR] File not found: {csv_path}")
    except ValueError as e:
        print(f"[ERROR] Bad CSV format/data: {e}")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")

    return categories, topups