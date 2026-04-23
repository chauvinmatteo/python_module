from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "eyeball", "frogs", "arsenic"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    res: str = dark_validate_ingredients(ingredients)
    return f"Dark spell '{spell_name}' {res}"
