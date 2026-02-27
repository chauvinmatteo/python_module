class GardenError(Exception):
    pass


class WaterError(GardenError):
    pass


class SunlightError(GardenError):
    pass


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if not plant_name:
        raise GardenError("Plant name cannot be empty!")
    if water_level < 1:
        raise WaterError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise WaterError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise SunlightError(f"Sunlight hours {sunlight_hours} is too low"
                            "(min 2)")
    if sunlight_hours > 12:
        raise SunlightError(f"Sunlight hours {sunlight_hours} is too high"
                            "(max 12)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_check() -> None:
    print("Testing good values...")
    check_plant_health("tomato", 5, 10)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 10)
    except GardenError as e:
        print(f"Error: {e}")
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 10)
    except GardenError as e:
        print(f"Error: {e}")
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 1)
    except GardenError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_check()
    print("\nAll error raising tests completed!")
