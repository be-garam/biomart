# 다운로드 가능한 링크 정보를 config/download_info.json에 저장하고 업데이트

import requests
import json
import os
from datetime import datetime

BASE_URL = "https://rest.ensembl.org"

def get_latest_release():
    response = requests.get(f"{BASE_URL}/info/data", headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        data = response.json()
        return max(release['version'] for release in data['releases'])
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