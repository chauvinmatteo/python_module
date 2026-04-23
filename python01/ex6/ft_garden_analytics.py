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

    def get_bonus(self) -> int:
        """This function gives a bonus reward to the class."""
        return 0

    def get_info(self) -> str:
        """This function gives the name and the size of a plant."""
        return f"- {self.name}: {self.height}cm, {self.age} days."


class FloweringPlant(Plant):
    """Represents a plant that produces colored flowers.
    Inherits from Plant."""
    def __init__(self, name: str, height: int, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def get_bonus(self) -> int:
        return 10

    def get_info(self) -> str:
        return (f"- {self.name}: {self.height}cm, {self.age} days, "
                f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """A high-value flower used for competitions with extra points. Inherits
    from FloweringPlant."""
    def __init__(self, name: str, height: int, age: int, color: str,
                 prize_point: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_point: int = prize_point

    def get_bonus(self) -> int:
        return 10 + self.prize_point

    def get_info(self) -> str:
        """This function gives info about the plant.
        We add the flower info to print the same thing as
        the FloweringPlant Class."""
        flower_info: str = super().get_info()
        return f"{flower_info}, Prize points: {self.prize_point}\n"


class GardenManager:
    """Registers a new plant to the manager's list using list concatenation."""
    total_garden = 0

    def __init__(self, owner_name: str) -> None:
        self.owner_name: str = owner_name
        self.plants: list = []
        GardenManager.total_garden += 1

    def add_plant(self, plant) -> None:
        """This function adds plant in the garden manager"""
        self.plants = self.plants + [plant]
        print(f"Added {plant.name} to {self.owner_name}'s Garden")

    class GardenStats:
        @staticmethod
        def calculate_score(plants) -> int:
            """Iterates through plants to calculate a total score based on
            height and bonuses."""
            score = 0
            for plant_point in plants:
                score += plant_point.height + plant_point.get_bonus()
            return score

        @staticmethod
        def validate_height(height) -> bool:
            """This function check is the height is valid."""
            if height >= 0:
                return True
            else:
                return False

        @staticmethod
        def get_full_info(plants) -> None:
            """Manually counts plant types and total additions.
            Prints a formatted summary of the garden's composition."""
            reg: int = 0
            flow: int = 0
            prize: int = 0
            total: int = 0

            for plant in plants:
                total += 1
                class_name: str = plant.__class__.__name__
                if class_name == "Plant":
                    reg += 1
                if class_name == "FloweringPlant":
                    flow += 1
                if class_name == "PrizeFlower":
                    prize += 1
            print(f"Plants Added: {total}, Total growth: {total}cm")
            print(f"Plant types: {reg} regular, {flow} flowering, "
                  f"{prize} prize flowers")

    @classmethod
    def create_garden_network(cls, names) -> list[list]:
        """This function is made to create multiple garden easily."""
        return [cls(name) for name in names]


def main() -> None:
    print("=== Garden Management System Demo ===\n")
    managers: list[GardenManager] = GardenManager.create_garden_network(
        ["Alice", "Bob"])
    alice: list = managers[0]
    bob: list = managers[1]

    p1 = Plant("Oak Tree", 100, 200)
    p2 = FloweringPlant("Rose", 25, 15, "red")
    p3 = PrizeFlower("Sunflower", 50, 45, "yellow", 10)
    p4 = Plant("Bamboo", 85, 70)
    alice.add_plant(p1)
    alice.add_plant(p2)
    alice.add_plant(p3)
    bob.add_plant(p4)
    print(f"\n{alice.owner_name} is helping all plants grow...")
    for plant in alice.plants:
        plant.height += 1
        plant.age += 1
        print(f"{plant.name} grew 1cm")
    print(f"\n{bob.owner_name} is helping all plants grow...")
    p4.age += 1
    p4.height += 1
    print(f"{p4.name} grew 1cm")
    print("\n=== Alice's Garden Report ===")
    for plant in alice.plants:
        print(f"{plant.get_info()}")
    GardenManager.GardenStats.get_full_info(alice.plants)
    print("\n=== Bob's Garden Report ===")
    print(f"{p4.get_info()}\n")
    GardenManager.GardenStats.get_full_info(bob.plants)
    score_alice: int = GardenManager.GardenStats.calculate_score(alice.plants)
    score_bob: int = GardenManager.GardenStats.calculate_score(bob.plants)
    is_valid: bool = GardenManager.GardenStats.validate_height(p1.height)
    print(f"\nHeight validation test: {is_valid}")
    print(f"Garden scores - Alice: {score_alice}, Bob: {score_bob}")
    print(f"Total gardens managed: {GardenManager.total_garden}")


if __name__ == "__main__":
    main()
