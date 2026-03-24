def absolute_import() -> None:
    from alchemy.transmutation import basic
    print(f"lead_to_gold(): {basic.lead_to_gold()}")
    print(f"stone_to_gem(): {basic.stone_to_gem()}")


def relative_import() -> None:
    from alchemy.transmutation import advanced
    print(f"philosophers_stone(): {advanced.philosophers_stone()}")
    print(f"elixir_of_life(): {advanced.elixir_of_life()}")


def package_acces() -> None:
    import alchemy.transmutation
    print("alchemy.transmutation.lead_to_gold():"
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone():"
          f"{alchemy.transmutation.philosophers_stone}")


def main() -> None:
    print("\n=== Pathway Debate Mastery ===")
    print()

    print("Testing Absolute Imports (from basic.py):")
    absolute_import()
    print()

    print("Testing Relative Imports (from advanced.py):")
    relative_import()
    print()

    print("Testing Package Access:")
    package_acces()
    print()

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
