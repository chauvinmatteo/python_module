import alchemy


def direct_module() -> None:
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())


def package_level() -> None:
    print("alchemy.elements.create_fire():", alchemy.create_fire())
    print("alchemy.elements.create_water():", alchemy.create_water())
    try:
        print("alchemy.elements.create_earth():", alchemy.create_earth())
    except AttributeError:
        print("alchemy.elements.create_earth(): AttributeError - not exposed")
    try:
        print("alchemy.elements.create_air():", alchemy.create_air())
    except AttributeError:
        print("alchemy.elements.create_air(): AttributeError - not exposed")


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===")
    print()

    print("Testing direct module access:")
    direct_module()
    print()
    print("Testing package-level access (controlled by __init__.py):")
    package_level()
    print()
    print("Package metadata:")
    print("Version: ", alchemy.__version__)
    print("Author: ", alchemy.__author__)


if __name__ == "__main__":
    main()
