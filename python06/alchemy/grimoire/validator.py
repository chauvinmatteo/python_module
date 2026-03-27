def validate_ingredients(ingredients: str) -> str:
    
    elements = ("fire", "water", "earth", "air")
    each_ingredients = ingredients.split(" ")
    for ingredients in each_ingredients:
        if ingredients in elements:
            return f"{ingredients} - VALID"
        else:
            return f"{ingredients} - INVALID"