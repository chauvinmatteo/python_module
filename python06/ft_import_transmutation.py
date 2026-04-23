def full_module() -> None:
    import alchemy
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())


def specific_import() -> None:
    from alchemy.elements import create_water
    print("create_water():", create_water())


def aliased_import() -> None:
    from alchemy.potions import healing_potion as heal
    print(f"heal(): {heal()}")


def multiple_import() -> None:
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion
    print("create_earth():", create_earth())
    print("create_fire():", create_fire())
    print("strength_potion():", strength_potion())


def main() -> None:
    print("\n=== Import Transmutation Mastery ===")
    print()

    print("Method 1 - Full module import:")
    full_module()
    print()

    print("Method 2 - Specific function import:")
    specific_import()
    print()

    print("Method 3 - Aliased import:")
    aliased_import()
    print()

    print("Method 4 - Multiple imports:")
    multiple_import()
    print()

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
