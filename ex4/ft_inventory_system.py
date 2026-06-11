#!/usr/bin/env python3

import sys


def main() -> None:
    args: list[str] = sys.argv

    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}
    total_quantity: int = 0
    most_abundant: str = "None"
    most_abundant_num: int | None = None
    least_abundant: str = "None"
    least_abundant_num: int | None = None
    i: int = 1
    while i <= len(args) - 1:
        try:
            arg: list[str] = args[i].split(":")
            if len(arg) != 2:
                raise SyntaxError(f"Error - invalid parameter '{args[i]}'")
            if arg[0] in inventory:
                raise SyntaxError(f"Redundant item '{arg[0]}' - discarding")
            quantity: int = int(arg[1])
            inventory[arg[0]] = quantity
            total_quantity += quantity
            if most_abundant_num is None or most_abundant_num < quantity:
                most_abundant_num = quantity
                most_abundant = arg[0]
            if least_abundant_num is None or least_abundant_num > quantity:
                least_abundant_num = quantity
                least_abundant = arg[0]
        except ValueError as e:
            print(f"Quantity error for '{arg[0]}': {e}")
        except Exception as e:
            print(e)
        i += 1
    if len(inventory) == 0:
        print(
            "Usage: python3 ft_inventory_system.py "
            "<item1:quantity1> <item2:quantity2> ...\n"
            )
        return
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")
    for item in inventory.keys():
        if total_quantity > 0:
            print(
                f"Item {item} "
                f"represents {round(inventory[item]/total_quantity*100, 1)}%"
            )
        else:
            print(f"Item {item} represents 0%")
    print(
        f"Item most abundant: {most_abundant} "
        f"with quantity {most_abundant_num}")
    print(
        f"Item least abundant: {least_abundant} "
        f"with quantity {least_abundant_num}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
