from pathlib import Path
from file_handler import load_data
from purchases import load_purchases, save_purchases


# Project root = folder that contains this main.py
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

DEFAULT_CSV = DATA_DIR / "mobile_products.csv"
PURCHASES_FILE = BASE_DIR / "purchases.csv"


def prompt_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Invalid entry. Please enter a number.")


def show_categories(categories):
    print("\n=== Ticket Categories ===")
    for i, c in enumerate(categories, start=1):
        print(f"{i}. {c.title}")
    print("0. Back")


def show_topups(topups, category_title):
    filtered = [t for t in topups if t.category_title == category_title]
    print(f"\n=== TopUps for {category_title} ===")
    for i, t in enumerate(filtered, start=1):
        price_pounds = t.price_in_pence / 100
        print(f"{i}. {t.title} - £{price_pounds:.2f}")
    print("0. Back")
    return filtered


def show_cart(purchases):
    print("\n=== Cart / Purchases This App ===")
    if not purchases:
        print("No purchases yet.")
        return

    total_pence = 0
    for i, p in enumerate(purchases, start=1):
        line_total = int(p["price_in_pence"]) * int(p["quantity"])
        total_pence += line_total
        print(f"{i}. {p['topup_title']} | Qty: {p['quantity']} | Line: £{line_total/100:.2f}")

    print(f"TOTAL: £{total_pence/100:.2f}")


def main():
    # 1) CSV path (desktop: fixed in data/)
    csv_path = DEFAULT_CSV

    if not csv_path.is_file():
        print(f"[ERROR] CSV not found: {csv_path}")
        print("Put the file here: <project>/data/mobile_products.csv")
        return

    # 2) Load data
    categories, topups = load_data(str(csv_path))
    if not categories:
        print("No categories loaded.")
        return

    # 3) Load saved purchases (if any)
    purchases = load_purchases(str(PURCHASES_FILE))

    while True:
        print("\n=== Bus Ticket Purchase System ===")
        print("1. Browse categories & buy")
        print("2. View cart / purchases")
        print("3. Save purchases now")
        print("0. Exit (auto-save)")
        choice = prompt_int("Choose: ")

        if choice == 1:
            while True:
                show_categories(categories)
                c = prompt_int("Select category: ")
                if c == 0:
                    break
                if c < 1 or c > len(categories):
                    print("Invalid choice.")
                    continue

                selected_category = categories[c - 1]

                while True:
                    filtered_topups = show_topups(topups, selected_category.title)
                    t = prompt_int("Select topup: ")
                    if t == 0:
                        break
                    if t < 1 or t > len(filtered_topups):
                        print("Invalid choice.")
                        continue

                    selected_topup = filtered_topups[t - 1]
                    price = selected_topup.price_in_pence / 100

                    print("\n--- TopUp Details ---")
                    print("Title:", selected_topup.title)
                    print("Price:", f"£{price:.2f}")
                    print("Entitlement type:", selected_topup.entitlement_type)
                    print("Unit:", selected_topup.entitlement_unit)
                    print("----------------------")

                    confirm = input("Buy this topup? (y/n): ").strip().lower()
                    if confirm == "y":
                        qty = prompt_int("Quantity (1..99): ")
                        if qty < 1 or qty > 99:
                            print("Quantity out of range.")
                            continue

                        purchases.append({
                            "category_title": selected_topup.category_title,
                            "topup_title": selected_topup.title,
                            "price_in_pence": selected_topup.price_in_pence,
                            "quantity": qty,
                        })

                        print("Added to cart.")
                    else:
                        print("Cancelled.")

        elif choice == 2:
            show_cart(purchases)

        elif choice == 3:
            save_purchases(str(PURCHASES_FILE), purchases)
            print(f"Saved to: {PURCHASES_FILE}")

        elif choice == 0:
            save_purchases(str(PURCHASES_FILE), purchases)
            print(f"Auto-saved to: {PURCHASES_FILE}")
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()