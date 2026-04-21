import sys

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()

    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
    return


ft_seed_inventory(sys.argv[1], int(sys.argv[2]), sys.argv[3])