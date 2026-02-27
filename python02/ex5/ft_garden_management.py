class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.name: str = name
        self.water_level: int = water_level
        self.sunlight_hours: int = sunlight_hours
        self.full_water: int = 10


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[Plant] = []

    def add_plants(self, name: str, water_level: int,
                   sunlight_hours: int) -> None:
        if name is None or not name:
            raise PlantError("Plant name cannot be empty")
        new_plant = Plant(name, water_level, sunlight_hours)
        self.plants.append(new_plant)
        print(f"Added {name} successfully")

    def watering_plant(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    raise WaterError("Cannot water None - invalid plant!")
                else:
                    print(f"Watering {plant.name} - succes")
        except WaterError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, plant: Plant) -> None:
        if plant.water_level > plant.full_water:
            raise WaterError(f"Water level {plant.water_level} is too high"
                             "(max 10)")
        if plant.sunlight_hours > 12:
            raise PlantError(f"Sunlight hours {plant.sunlight_hours} is too "
                             "high (max 12)")
        if plant.sunlight_hours < 2:
            raise PlantError(f"Sunlight hours {plant.sunlight_hours} is to low"
                             "(min 2)")
        if plant.water_level < 1:
            raise WaterError(f"Water level {plant.water_level} is too low"
                             "(min 1)")
        print(f"{plant.name}: healthy (water: {plant.water_level},"
              f"sun: {plant.sunlight_hours})")


def test_garden_management() -> None:
    manager = GardenManager()
    print("Adding plant to garden...")
    garden: list[tuple[str, int, int]] = [("tomato", 5, 8), ("lettuce", 15, 4),
                                          ("", 4, 10)]
    for name, water, sun in garden:
        try:
            manager.add_plants(name, water, sun)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    try:
        manager.watering_plant()
    except WaterError as e:
        print(f"Error: {e}")
    print("\nChecking plant health...")
    for plant in manager.plants:
        try:
            manager.check_health(plant)
        except (ValueError, WaterError, PlantError) as e:
            print(f"Error checking {plant.name}: {e}")
    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
    print("Garden management system test complete!")
