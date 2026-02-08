def ft_garden_intro() -> None:
    """This function display information about a plant in my garden.
       Each variable gives the information needed about the plant.
       We use a print to call for each variable."""
    name: str = "Rose"
    height: int = 25
    age: int = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
