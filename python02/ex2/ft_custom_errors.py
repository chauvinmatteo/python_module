class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(name: str, age: int, water_level: int) -> None:
    if age > 50:
        raise PlantError(f"The {name} plant is wilting!")
    elif age < 0:
        raise PlantError(f"The {name} plant age can't be negative!")
    if water_level < 5:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        check_plant("tomato", 80, 10)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        check_plant("tomato", 30, 2)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", 80, 10)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_plant("tomato", 30, 2)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")
