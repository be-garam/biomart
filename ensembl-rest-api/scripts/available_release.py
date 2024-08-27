# scripts/available_releases.py

import re
from ftplib import FTP
import json
import os

FTP_HOST = 'ftp.ensembl.org'
FTP_PATH = '/pub'
CONFIG_PATH = 'config/available_releases.json'

def get_releases_from_ftp():
    ftp = FTP(FTP_HOST)
    ftp.login()
    ftp.cwd(FTP_PATH)

    releases = []
    pattern = re.compile(r'release-(\d+)')

    def process_line(line):
        match = pattern.search(line)
        if match:
            releases.append(int(match.group(1)))

    ftp.retrlines('LIST', process_line)
    ftp.quit()

    releases = list(set(releases))
    return sorted(releases, reverse=True)

def update_available_releases():
    releases = get_releases_from_ftp()
    
    config_dir = os.path.dirname(CONFIG_PATH)
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    with open(CONFIG_PATH, 'w') as f:
        json.dump({"releases": releases}, f, indent=2)
    
    print(f"Updated available releases. Total releases: {len(releases)}")

def main():
    update_available_releases()

if __name__ == '__main__':
    main()