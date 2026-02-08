class Plant:
    """Represents a garden plant with its growth characteristics.
    Attributes:
        name (str): The name of the plant species.
        height (int): The height of the plant in centimeters.
        age (int): The age of the plant in days."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


def main() -> None:
    """In the main we gives value to each plant and print them."""
    plant_list: list[list] = [
        ["Rose", 25, 30],
        ["Sunflower", 80, 45],
        ["Cactus", 15, 120]
    ]
    print("=== Garden Plant Registry ===")
    for data in plant_list:
        plant = Plant(*data)
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    main()
