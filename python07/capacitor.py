import ex1
from ex1.capability import HealCapability, TransformCapability
from ex0 import Creature


def test_healing(factory: ex1.HealingCreatureFactory) -> None:

    print(" base:")
    base: Creature = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())

    print(" evolved:")
    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_transform(factory: ex1.TransformCreatureFactory) -> None:

    print(" base:")
    base: Creature = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print(" evolved:")
    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


def main() -> None:
    print("Testing Creature with healing capability")
    test_healing(ex1.HealingCreatureFactory())

    print("\nTesting Creature with transform capability")
    test_transform(ex1.TransformCreatureFactory())


if __name__ == "__main__":
    main()
