from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    if any(item.lower() in ingredients.lower() for item in allowed):
        return f"with {ingredients}: VALID"
    return f"with {ingredients}: INVALID"
