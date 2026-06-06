#!/usr/bin/env python3

import sys

def main() -> None:
    args:list = sys.argv

    print("=== Inventory System Analysis ===")

    inventory: dict = {}
    total_quantity: int = 0
    most_abundant_num: int = 0 
    least_abundant_num: int = 0
    i: int = 1
    while i <= len(args) - 1:
        try:
            arg: list = args[i].split(":")
            if len(arg) != 2:
                raise ValueError(f"Error - invalid parameter '{args[i]}'")
            for item in inventory.keys():
                if arg[0] == item:
                    raise ValueError(f"Redundant item '{item}' - discarding")
            quantity: int = int(arg[1])
            inventory[arg[0]] = quantity
            total_quantity += quantity
            if most_abundant_num < quantity:
                most_abundant_num = quantity
                most_abundant: str = arg[0]
            if least_abundant_num == 0 and quantity != 0:
                least_abundant_num = quantity
                least_abundant: str = arg[0]
            elif least_abundant_num > quantity:
                least_abundant_num = quantity
                least_abundant = arg[0]
        except Exception as e:
            print(e)
        i += 1

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")
    for item in inventory.keys():
        print(
            f"Item {item} "
            f"represents {round(inventory[item]/total_quantity*100,1)}%"
            )
    print(f"Item most abundant: {most_abundant} with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} with quantity {inventory[least_abundant]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
        

if __name__ == "__main__":
    main()
