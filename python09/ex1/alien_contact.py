from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional, Any, Self


class ContactType(str, Enum):
    RAD = "radio"
    VIS = "visual"
    PHY = "physical"
    TEL = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minute: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_alien_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID needs to start with 'AC'")

        if self.contact_type == ContactType.PHY and not self.is_verified:
            raise ValueError("Physical contact needs to be verified")

        if self.contact_type == ContactType.TEL and self.witness_count < 3:
            raise ValueError("Telepathic contact needs at least 3 witnesses")

        if self.signal_strength > 7 and not self.message_received:
            raise ValueError("Received message is mandatory"
                             "if signal strengh is over 7")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("========================================")

    try:
        valid_data: dict[str, Any] = {
            "contact_id": "AC_2024_001",
            "timestamp": datetime.now(),
            "location": "Area 51, Nevada",
            "contact_type": "radio",
            "signal_strength": 8.5,
            "duration_minute": 45,
            "witness_count": 5,
            "message_received": "Greetings from Zeta Reticuli"
        }

        contact = AlienContact(**valid_data)

        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minute} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")

    except ValidationError as e:
        print(f"Erreur inattendue : {e}")

    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_data: dict[str, Any] = {
            "contact_id": "AC_2024_002",
            "timestamp": datetime.now(),
            "location": "Moon Base",
            "contact_type": "telepathic",
            "signal_strength": 4.0,
            "duration_minute": 10,
            "witness_count": 1,
            "is_verified": True
        }
        invalid_contact = AlienContact(**invalid_data)
        if invalid_contact:
            print("Second contact is valid aswell")
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
