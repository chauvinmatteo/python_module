from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    
    res = validate_ingredients(ingredients)
    if "VALID" in res:
        return f"Spell recorded: {spell_name} ({res})"
    else:
        return f"Spell rejected: {spell_name} ({res})"