from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Self, Any


class CrewRank(Enum):
    CAD = "cadet"
    OFF = "officer"
    LIE = "lieutenant"
    CAP = "captain"
    COM = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID needs to start with 'M'")

        has_leader: bool = any(m.rank in [CrewRank.COM, CrewRank.CAP]
                               for m in self.crew)
        if not has_leader:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced: list[CrewMember] = [m for m in self.crew
                                             if m.years_experience >= 5]
            if len(experienced) / len(self.crew) < 0.5:
                raise ValueError("Long missions (> 365 days) need 50%"
                                 "experienced crew (5+ years)")

        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        valid_mission: dict[str, Any] = {
            'mission_id': 'M2024_EUROPA',
            'mission_name': 'Saturn Rings Research Mission',
            'destination': 'Saturn Rings',
            'launch_date': '2024-09-18T00:00:00',
            'duration_days': 602,
            'crew': [
                {
                    'member_id': 'CM041',
                    'name': 'William Davis',
                    'rank': 'captain',
                    'age': 35,
                    'specialization': 'Medical Officer',
                    'years_experience': 14,
                    'is_active': True
                },
                {
                    'member_id': 'CM042',
                    'name': 'Sarah Smith',
                    'rank': 'captain',
                    'age': 55,
                    'specialization': 'Research',
                    'years_experience': 30,
                    'is_active': True
                },
                {
                    'member_id': 'CM043',
                    'name': 'Elena Garcia',
                    'rank': 'commander',
                    'age': 18,
                    'specialization': 'Research',
                    'years_experience': 30,
                    'is_active': True
                }
            ],
            'mission_status': 'planned',
            'budget_millions': 1092.6
        }
        mission = SpaceMission(**valid_mission)

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Status: {mission.mission_status}")
        print("Crew Members:")
        for m in mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")
    except ValidationError as e:
        print("\n--- Mission Validation Failed ---")
        for error in e.errors():
            path = error['loc']
            msg = error['msg']
            if len(path) >= 3 and path[0] == 'crew':
                index = path[1]
                field = path[2]
                if isinstance(index, int):
                    print(f"Error on Crew Member #{index + 1}"
                          f"(Field: '{field}'): {msg}")
            else:
                print(f"Error on {path[-1]}: {msg}")

    print("\n=========================================")
    print("Expected validation error:")

    try:
        invalid_mission: dict[str, Any] = {
            'mission_id': 'M2024_EUROPA',
            'mission_name': 'Saturn Rings Research Mission',
            'destination': 'Saturn Rings',
            'launch_date': '2024-09-18T00:00:00',
            'duration_days': 602,
            'crew': [
                {
                    'member_id': 'CM041',
                    'name': 'William Davis',
                    'rank': 'officer',
                    'age': 35,
                    'specialization': 'Medical Officer',
                    'years_experience': 14,
                    'is_active': True
                },
                {
                    'member_id': 'CM042',
                    'name': 'Sarah Smith',
                    'rank': 'cadet',
                    'age': 55,
                    'specialization': 'Research',
                    'years_experience': 30,
                    'is_active': True
                },
                {
                    'member_id': 'CM043',
                    'name': 'Elena Garcia',
                    'rank': 'lieutenant',
                    'age': 18,
                    'specialization': 'Research',
                    'years_experience': 30,
                    'is_active': True
                }
            ],
            'mission_status': 'planned',
            'budget_millions': 1092.6
        }
        invalid = SpaceMission(**invalid_mission)
        if invalid:
            print(invalid.mission_name)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
