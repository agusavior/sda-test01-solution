from dataclasses import dataclass
from typing import List


@dataclass
class Superheroe:
    id: int
    full_name: str
    alter_egos: str
    aliases: List[str]
    place_of_birth: str
    image_url: str
    occupation_description: str

    # Not case sensitive.
    # Get if the superhero is from a given occupation.
    def has_specific_occupation(self, occupation: str) -> bool:
        return occupation.upper() in self.occupation_description.upper()
