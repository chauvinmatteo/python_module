from alchemy import grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    spell = "Fantasy"
    ingredients = "Earth, wind and fire"
    result: str = grimoire.light_spell_record(spell, ingredients)
    print(f"Testing record light spell: {result}")


if __name__ == "__main__":
    main()
