import requests
import json
import os

BASE_URL = "https://rest.ensembl.org"

def load_species_info():
    with open("config/species_info.json", "r") as f:
        return json.load(f)

def get_assembly_info(species):
    response = requests.get(f"{BASE_URL}/info/assembly/{species}", 
                            headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch assembly information for {species}")
        return None

def update_species_assembly_info():
    species_list = load_species_info()
    updated_info = []

    for species in species_list:
        species_name = species['name']
        print(f"Processing {species_name}...")
        
        assembly_info = get_assembly_info(species_name)
        if assembly_info:
            species['assembly_info'] = {
                'assembly_name': assembly_info.get('assembly_name'),
                'assembly_date': assembly_info.get('assembly_date'),
                'assembly_accession': assembly_info.get('assembly_accession'),
                'genebuild_last_geneset_update': assembly_info.get('genebuild_last_geneset_update')
            }
        
        updated_info.append(species)

    return updated_info

def save_updated_info(updated_info):
    with open("config/species_assembly_info.json", "w") as f:
        json.dump(updated_info, f, indent=2)

def main():
    updated_info = update_species_assembly_info()
    save_updated_info(updated_info)
    print(f"Updated information for {len(updated_info)} species")

if __name__ == "__main__":
    main()