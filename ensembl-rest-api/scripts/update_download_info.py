# 다운로드 가능한 링크 정보를 config/download_info.json에 저장하고 업데이트

import json
import os
from ftplib import FTP

FTP_SERVER = "ftp.ensembl.org"
BASE_PATH = "/pub/release-{release}/fasta/{species}/dna/"

def load_species_assembly_info():
    with open("config/species_assembly_info.json", "r") as f:
        return json.load(f)

def check_file_exists(ftp, filename):
    try:
        ftp.size(filename)
        return True
    except:
        return False

def generate_download_info():
    species_info = load_species_assembly_info()
    download_info = {}

    with FTP(FTP_SERVER) as ftp:
        ftp.login()
        
        for species in species_info:
            species_name = species['name']
            assembly_name = species['assembly']
            # assembly_info = species[.get('assembly_info', {})]
            # assembly_name = assembly_info.get('assembly_name')
            release = species['release']

            if not assembly_name:
                print(f"Warning: No assembly information for {species_name}")
                continue

            ftp_path = BASE_PATH.format(release=release, species=species_name)
            try:
                ftp.cwd(ftp_path)
            except:
                print(f"Warning: FTP path not found for {species_name}")
                continue

            download_info[species_name] = {"release": release, "assembly": assembly_name, "files": {}}

            # for seq_type in ['dna', 'dna_sm', 'dna_rm']:
            for seq_type in ['dna']:
                for id_type in ['toplevel', 'primary_assembly']:
                    f_species_name = species_name[0].upper() + species_name[1:]
                    filename = f"{f_species_name}.{assembly_name}.{seq_type}.{id_type}.fa.gz"
                    if check_file_exists(ftp, filename):
                        url = f"https://{FTP_SERVER}{ftp_path}{filename}"
                        download_info[species_name]["files"][f"{seq_type}_{id_type}"] = url
                        print(f"Added {seq_type}_{id_type} for {species_name}")

            if not download_info[species_name]["files"]:
                print(f"Warning: No files found for {species_name}")
                print(f"url: {url}")
                del download_info[species_name]

    return download_info

def save_download_info(download_info):
    with open("config/download_info.json", "w") as f:
        json.dump(download_info, f, indent=2)

def main():
    download_info = generate_download_info()
    save_download_info(download_info)
    print(f"Updated download information for {len(download_info)} species")

if __name__ == "__main__":
    main()