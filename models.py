from dataclasses import dataclass

@dataclass(frozen=True)
class Category:
    title: str
    description: str

@dataclass(frozen=True)
class TopUp:
    category_title: str
    title: str
    description: str
    price_in_pence: int
    entitlement_type: str
    entitlement_unit: str
    entitlement_value: str
    entitlement_quantity: str
    passenger_class_name: str
    passenger_class_quantity: str