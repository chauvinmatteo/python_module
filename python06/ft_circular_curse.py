from alchemy.grimoire import validate_ingredients, record_spell


def check_ingredients():
    print(f"validate_ingredients(\"fire air\"): {validate_ingredients("fire air")}")
    print(f"validate_ingredients(\"dragon scale\"): {validate_ingredients("dragon scale")}")


def check_spell():
    print(f"record_spell(\"Fireball\", \"fire air\"): {record_spell("Fireball", "fire air")}")
    print(f"record_spell(\"Dark Magic\", \"shadow\"): {record_spell("Dark Magic", "shadow")}")


def main():
    print("\n=== Circular Curse Breaking ===")
    print()

    print("Testing ingredient validation:")
    check_ingredients()
    print()

    print("Testing spell recording with validation:")
    check_spell()
    print()

    print("Testing late import technique:")
    print(f"record_spell(\"Lightning\", \"air\"): {record_spell("Lightning", "air")}")
    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
