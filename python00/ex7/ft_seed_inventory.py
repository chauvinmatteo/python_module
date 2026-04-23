def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seeds = str.capitalize(seed_type)
    if unit == "packets":
        print(seeds, "seeds:", quantity, "packets available")
    elif unit == "area":
        print(seeds, "seeds:", "covers", quantity, "square meters")
    elif unit == "grams":
        print(seeds, "seeds:", quantity, "grams total")
    else:
        print(seeds, "seeds:", "Unknown unit type")
