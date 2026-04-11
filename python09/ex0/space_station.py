from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        valid_station = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": datetime.now(),
            "is_operational": True,
        }

        station = SpaceStation(**valid_station)

        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        status = "Operational" if station.is_operational else "Non-Operational"
        print(f"Status: {status}")
    except ValidationError as e:
        print(e)
    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_station = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 25,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": datetime.now(),
            "is_operational": True,
            "notes": "test"
        }

        station2 = SpaceStation(**invalid_station)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
