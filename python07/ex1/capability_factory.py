from ex0.factory import CreatureFactory
from ex1.capability import (
    Sproutling, Bloomelle, Shiftling, Morphagon,
    TransformCapability, HealCapability
)


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> HealCapability:
        return Sproutling()

    def create_evolved(self) -> HealCapability:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> TransformCapability:
        return Shiftling()

    def create_evolved(self) -> TransformCapability:
        return Morphagon()
