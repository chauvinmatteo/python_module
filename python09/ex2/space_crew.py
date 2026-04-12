from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional


class CrewRank(Enum):
    CAD = "cadet"
    OFF = "officer"
    LIE = "lieutenant"
    CAP = "captain"
    COM = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length = 3, max_length = 10)
    name: str = Field(min_length = 2, max_length = 50)
    rank: CrewRank
    age: int = Field(ge = 18, le = 80)
    specialization: str = Field(min_length = 3, max_length = 30)
    years_experience: int = Field(ge = 0, le = 50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length = 5, max_length = 15)
    mission_name: str = Field(min_length = 3, max_length = 100)
    destination: str = Field(min_length = 3, max_length = 50)
    launch_date: datetime
    duration_days: int = Field(ge = 1, le = 3650)
    crew: list[CrewMember] = Field(ge = 1, le = 12)
    mission_status: str = "planned"
    budget_millions: float = Field(min_length = 1.0, max_length = 10000.0)

    @model_validator(mode='after')
    def validate_mission(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID needs to start with 'M'")
        
        has_leader = any(m.rank in [CrewRank.COM, CrewRank.CAP] for m in self.crew)
        if not has_leader:
            raise ValueError("Must have at least one Commander or Captain")
        
        if self.duration_days > 365:
            experienced = [m for m in self.crew if m.years_experience >= 5]
            if len(experienced) / len(self.crew) < 0.5:
                raise ValueError("Long missions (> 365 days) need 50%"
                                 "experienced crew (5+ years)")
        
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")


def main():
    pass


if __name__ == "__main__":
    main()