import sys


def parsing(inventory_content: list[str]) -> dict[str, int]:
    my_inventory: dict[str, int] = {}
    for arg in inventory_content:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        parts: list[str] = arg.split(":")
        name: str = parts[0]
        raw_quantity: str = parts[1]
        if name in my_inventory.keys():
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity = int(raw_quantity)
            if quantity <= 0:
                print(f"Error: Item '{name}' must have a positive quantity"
                      f"(got {quantity})")
                continue
            items: dict[str, int] = {name: quantity}
            my_inventory.update(items)
        except ValueError as e:
            print(f"Quantity error for '{name}' : {e}")
    return my_inventory


def current_inventory(my_inventory: dict[str, int]) -> None:
    inventory_list: list[str] = list(my_inventory.keys())
    print(f"Item list: {inventory_list}")


def inventory_data(my_inventory: dict[str, int]) -> None:
    value_sum: int = sum(my_inventory.values())
    if value_sum == 0:
        print("Inventory is empty or all quantities are zero.")
        return
    max_qty: int = 0
    min_qty: int = -1
    most_item: str = ""
    least_item: str = ""
    for items in my_inventory.keys():
        qty: int = my_inventory[items]
        percentage: float = my_inventory.get(items, qty) / value_sum
        print(f"Item {items} represents {(percentage * 100):.1f}%")
        if qty > max_qty:
            max_qty = qty
            most_item = items
        if min_qty == -1 or qty < min_qty:
            min_qty = qty
            least_item = items
    print(f"Item most abundant: {most_item} with quantity {max_qty}")
    print(f"Item least abundant: {least_item} with quantity {min_qty}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    my_inventory: dict[str, int] = parsing(sys.argv[1:])
    if my_inventory:
        print(f"Got inventory: {my_inventory}")
        current_inventory(my_inventory)
        print(f"Total quantity of the {len(my_inventory)} "
            f"items: {sum(my_inventory.values())}")
    inventory_data(my_inventory)
    my_inventory.update({"magic_item": 1})
    print(f"Updated inventory: {my_inventory}")


if __name__ == "__main__":
    main()
