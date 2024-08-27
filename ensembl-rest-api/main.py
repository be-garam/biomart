# 사용자 입력에 따라 FASTA 파일을 다운로드

import argparse
import json
import os
import subprocess

def load_download_info():
    with open("config/download_info.json", "r") as f:
        return json.load(f)

def download_fasta(release, species, file_type):
    download_info = load_download_info()
    if release not in download_info or species not in download_info[release]:
        print(f"No download information for release {release} and species {species}")
        return

    url = download_info[release][species][file_type]
    output_dir = f"downloads/release-{release}/{species}"
    os.makedirs(output_dir, exist_ok=True)
    
    subprocess.run(["wget", "-P", output_dir, url])
    print(f"Downloaded {file_type} FASTA for {species} (release {release})")

def main():
    parser = argparse.ArgumentParser(description="Download Ensembl FASTA files")
    parser.add_argument("--release", required=True, help="Ensembl release version")
    parser.add_argument("--species", required=True, help="Species name")
    parser.add_argument("--type", choices=["dna", "cdna", "ncrna"], required=True, help="FASTA file type")
    args = parser.parse_args()

    download_fasta(args.release, args.species, args.type)

if __name__ == "__main__":
    main()