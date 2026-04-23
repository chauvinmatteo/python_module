class Plant:
    """Represents a garden plant with its growth characteristics.
    Attributes:
        name (str): The name of the plant species.
        height (int): The height of the plant in centimeters.
        days_old (int): The age of the plant in days."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        """This function is used to print the name, height and age of each
    plant that we created."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    """Main entry point of the script.
      Initialize a plant value and create them to
      be able to use them straight away."""
    print("=== Plant Factory Output ===")
    plant_list: list[list] = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    plant_created: int = 0
    for data in plant_list:
        plant = Plant(*data)
        plant.get_info()
        plant_created = plant_created + 1
    print(f"\nTotal plants created: {plant_created}")


if __name__ == "__main__":
    main()
