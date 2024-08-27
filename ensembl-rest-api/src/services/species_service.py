from src.utils.api_utils import get_json_from_api
from src.utils.file_utils import save_json
from src.models.species import Species

class SpeciesService:
    def __init__(self):
        self.species_file = "config/species_info.json"

    def update_species_info(self):
        species_data = get_json_from_api("info/species")
        species_list = [Species(s['name'], s['display_name'], s['release']) for s in species_data['species']]
        save_json([vars(s) for s in species_list], self.species_file)
        return species_list