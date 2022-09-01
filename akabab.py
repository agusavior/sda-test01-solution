from typing import Any, Dict, List
import requests
import json
from config import *
from superheroe import Superheroe

BASE_URL = 'https://akabab.github.io/superhero-api/api'
NONE_OCUPATION = '-'

# Documentation:  https://akabab.github.io/superhero-api/api/
class AkababAPI:
    @classmethod
    def get_all(cls) -> List[Superheroe]:
        # Url
        url = f'{BASE_URL}/all.json'
        
        # Response
        response = requests.get(url=url)

        # Raise for status
        response.raise_for_status()

        # Get the list of every supehero (in dict format)
        ds = json.loads(response.content)

        # Convert every json data to python defined model
        return [
            cls.from_data_to_superheroe(d)
            for d in ds
        ]

    # Warning! Mocked endpoint!
    @classmethod
    def get_all_occupations(cls):
        # Print a warning
        print('Warning. You are using a mocked endpoint. Implement an endpoint or make in order to get all occupations.')
        
        return [
            'musician',
            'adventurer',
            'author',
            'investigator',
            'professor',
            'criminal',
            'mercenary',
            'commander',
            'soldier',
            'archaelogist',
            'ambassador',
            'janitor',
            'pirate',
            'terrorist',
            'fighter',
        ]

    @classmethod
    def from_data_to_superheroe(cls, d: Dict[Any, Any]) -> Superheroe:
        # Decontruct
        id = d['id']
        full_name = d['biography']['fullName'] or d['name']
        alter_egos = d['biography']['alterEgos']
        aliases = d['biography']['aliases']
        image_url = d['images']['sm']
        place_of_birth = d['biography']['placeOfBirth']
        occupation_description = d['work']['occupation']

        # Create instance of model
        superheroe = Superheroe(
            id=id,
            full_name=full_name,
            alter_egos=alter_egos,
            aliases=aliases,
            image_url=image_url,
            occupation_description=occupation_description,
            place_of_birth=place_of_birth,
        )

        return superheroe