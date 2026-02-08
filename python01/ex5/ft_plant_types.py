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


class Flower(Plant):
    """The Flower class inherits the features of the Plant class but
    adds the color variable."""
    def __init__(self, name, height, age, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """This function print that the flower is blooming."""
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    """The Tree class inherits the features of the Plant class but
    adds the trunk diameter variable."""
    def __init__(self, name, height, age, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        """This function is calculating the shading are of a tree."""
        shade: int = (self.height * self.trunk_diameter) / 100
        print(f"{self.name} provides {shade} square meters of shade\n")


class Vegetable(Plant):
    """The Vegetable class inherits the features of the Plant class but
        adds the harvest season and the nutritional value variables."""
    def __init__(self, name, height, age, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value


def main() -> None:
    """Starting point of the program.
    Initialize multiple plants from different class.
    See their common trait inherited from main class
    and differences between each others."""
    flower_list: list[Flower] = [
        Flower("Rose", 25, 30, "red"),
        Flower("Sunflower", 80, 45, "yellow")
    ]
    tree_list: list[Tree] = [
        Tree("Oak", 500, 128, 50),
        Tree("Bamboo", 300, 250, 35)
    ]
    vegetable_list: list[Vegetable] = [
        Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C"),
        Vegetable("Carrot", 20, 30, "autumn harvest", "vitamin A")
    ]
    print("=== Garden Plant Types ===\n")
    for flower in flower_list:
        print(f"{flower.name} (Flower): {flower.height}cm, {flower.age} days,"
              f"{flower.color}")
        flower.bloom()
    for tree in tree_list:
        print(f"{tree.name} (Tree): {tree.height}cm, {tree.age} days, "
              f"{tree.trunk_diameter}cm diameter")
        tree.produce_shade()
    for vegetable in vegetable_list:
        print(f"{vegetable.name} (Vegetable): {vegetable.height}cm, "
              f"{vegetable.age} days, {vegetable.harvest_season}")
        print(f"{vegetable.name} is rich in {vegetable.nutritional_value}")


if __name__ == "__main__":
    main()
