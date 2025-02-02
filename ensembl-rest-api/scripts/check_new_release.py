# 한 달에 한 번 새로운 릴리스를 확인하고 config/available_releases.json를 업데이트

import requests
import json
import os
from datetime import datetime

BASE_URL = "https://rest.ensembl.org"

def get_latest_release():
    ext = "/info/data/?"
    response = requests.get(BASE_URL+ext, headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data['releases'][0]
    else:
        raise Exception("Failed to fetch latest release information")

def update_available_releases(latest_release):
    file_path = "config/available_releases.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            releases = json.load(f)
    else:
        releases = []

    if latest_release not in releases:
        releases.append(latest_release)
        releases.sort(reverse=True)
        with open(file_path, "w") as f:
            json.dump(releases, f, indent=2)
        return True
    return False

def main():
    latest_release = get_latest_release()
    if update_available_releases(latest_release):
        print(f"New release {latest_release} added")
    else:
        print("No new release found")

if __name__ == "__main__":
    main()