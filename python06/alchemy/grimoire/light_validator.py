from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = light_spell_allowed_ingredients()
    if any(item.lower() in ingredients.lower() for item in allowed):
        return f"with {ingredients}: VALID"
    return f"with {ingredients}: INVALID"
