class SecurePlant:
    """We create the Plant class with name, heigh and age. We call
        the height and age with two underscore to protect them from
        being changed outside of the class definition."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.__height = 0
        self.__age = 0
        self.set_height(height, display_success=False)
        self.set_age(age, display_success=False)

    def get_height(self) -> int:
        """This function return the current height of the plant."""
        return self.__height

    def set_height(self, new_height: int, display_success=True) -> None:
        """This function is used to set the height of a plant to
            a different one, with a security to avoid negative value."""
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm"
                  " [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height: int = new_height
            if display_success:
                print(f"Height updated: {new_height}cm [OK]")

    def get_age(self) -> int:
        """This function return the current age of the plant."""
        return self.__age

    def set_age(self, new_age: int, display_success=True) -> None:
        """This function is used to set the age of a plant to
            a different one, with a security to avoid negative value."""
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days"
                  " [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age: int = new_age
            if display_success:
                print(f"Age updated: {new_age} days [OK]\n")


def main() -> None:
    """Main starting point.
    We create a plant and give them various value to
    see if they're valid or not."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {plant.name}")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"Current plant: {plant.name} ({plant.get_height()}cm, "
          f"{plant.get_age()} days)")


if __name__ == "__main__":
    main()
