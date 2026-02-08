class Plant:
    """Represents a garden plant with its growth characteristics.
    Attributes:
        name (str): The name of the plant species.
        height (int): The height of the plant in centimeters.
        days_old (int): The age of the plant in days."""
    def __init__(self, name: str, height: int, days_old: int) -> None:
        self.name: str = name
        self.height: int = height
        self.days_old: int = days_old

    def grow(self) -> None:
        """This function makes the plant grow by incrementig their
        height by 1."""
        self.height = self.height + 1

    def age(self) -> None:
        """This function makes the plant age by incrementig their
        age by 1."""
        self.days_old = self.days_old + 1

    def get_info(self) -> None:
        """This function serves as way to get the information about a plant
        at any given moment. By calling it we know the name, height and age
        of the plant at the moment."""
        print(f"{self.name}: {self.height}cm, {self.days_old} days old")


def main() -> None:
    """Main entry point of the script.
    Initializes a plant registry and simulates a week of growth
    to display the garden's evolution."""
    plant_list: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Day 1 ===")
    for data in plant_list:
        data.get_info()
    print("=== Day 7 ===")
    growing_rate: int = 0
    for current_day in range(1, 6 + 1):
        for data in plant_list:
            data.grow()
            data.age()
        growing_rate = growing_rate + 1
    for data in plant_list:
        data.get_info()
    print(f"Growth this week: +{growing_rate}cm")


if __name__ == "__main__":
    main()
