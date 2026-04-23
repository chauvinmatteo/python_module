import time
import functools
from typing import Callable, Any

def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = args[2] if len(args) > 2 else args[0]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator

def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"

@spell_timer
def fireball(power: int) -> str:
    time.sleep(0.1)
    return "Fireball cast!"

@retry_spell(max_attempts=3)
def unstable_spell():
    raise Exception("Mana leak")

def main():
    print("Testing spell timer...")
    res = fireball(50)
    print(f"Result: {res}")

    print("\nTesting retrying spell...")
    print(unstable_spell())
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("Al"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))

if __name__ == "__main__":
    main()