def garden_operations(error_choice: int) -> None:
    if error_choice == 0:
        raise ValueError
    elif error_choice == 1:
        raise ZeroDivisionError
    elif error_choice == 2:
        raise FileNotFoundError
    elif error_choice == 3:
        raise KeyError


def test_error_type() -> None:
    print("=== Garden Error Types Demo ===\n")
    try:
        garden_operations(0)
    except ValueError:
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()\n")
    try:
        garden_operations(1)
    except ZeroDivisionError:
        print("Testing ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        garden_operations(2)
    except FileNotFoundError:
        print("Testing FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    try:
        garden_operations(3)
    except KeyError:
        print("Testing KeyError...")
        print("Caught KeyError: 'missing\\_plant'\n")
    try:
        raise ValueError
    except Exception:
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_type()
