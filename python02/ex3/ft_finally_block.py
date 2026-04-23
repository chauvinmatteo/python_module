class GardenError(Exception):
    pass


class WaterError(GardenError):
    pass


def water_plants(plant_list: list[str]) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None or not plant:
                raise WaterError("Cannot water None - invalid plant!")
            else:
                print(f"Watering {plant}")
    except WaterError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(["tomato", "", "carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
