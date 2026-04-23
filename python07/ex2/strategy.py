from abc import ABC, abstractmethod
from typing import Any
from ex0 import Creature
from ex1.capability import TransformCapability, HealCapability


class InvalidStrategyException(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            return creature.attack()
        raise InvalidStrategyException(f"Battle error, aborting tournament: "
                                       f"Invalid Creature '{creature.name}' "
                                       "for this normal strategy")


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            c: Any = creature
            actions = [
                c.transform(),
                c.attack(),
                c.revert()
            ]
            return "\n".join(actions)
        raise InvalidStrategyException(f"Battle error, aborting tournament: "
                                       f"Invalid Creature '{creature.name}'"
                                       "for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            c: Any = creature
            actions = [
                c.attack(),
                c.heal()
            ]
            return "\n".join(actions)
        raise InvalidStrategyException(f"Battle error, aborting tournament: "
                                       f"Invalid Creature '{creature.name}'"
                                       "for this defensive strategy")
