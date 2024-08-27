# 모든 종 정보를 가져와 config/species_info.json에 저장

import requests
import json
import os

BASE_URL = "https://rest.ensembl.org"

def get_species_info():
    response = requests.get(f"{BASE_URL}/info/species", headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        return response.json()['species']
    else:
        raise Exception("Failed to fetch species information")

def save_species_info(species_info):
    with open("config/species_info.json", "w") as f:
        json.dump(species_info, f, indent=2)

def main():
    species_info = get_species_info()
    save_species_info(species_info)
    print(f"Saved information for {len(species_info)} species")

if __name__ == "__main__":
    main()