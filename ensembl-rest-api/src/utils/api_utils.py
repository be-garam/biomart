import requests

BASE_URL = "https://rest.ensembl.org"

def get_json_from_api(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}", headers={"Content-Type": "application/json"})
    response.raise_for_status()
    return response.json()