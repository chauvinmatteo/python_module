from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name, cost, rarity, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        game_state = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.type} summoned to battlefield"
        }
        return game_state

    def attack_target(self, target: Card) -> dict:
        attack_result: dict[str, str | int | bool] = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
        target.health -= self.attack
        if target.health <= 0:
            target.health = 0
        return attack_result

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return card_info
