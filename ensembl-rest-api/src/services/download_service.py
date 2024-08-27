import subprocess
from src.utils.file_utils import ensure_directory, load_json, save_json

class DownloadService:
    def __init__(self):
        self.download_info_file = "config/download_info.json"

    def update_download_info(self, releases, species_list):
        download_info = {}
        for release in releases:
            download_info[release.version] = {}
            for species in species_list:
                download_info[release.version][species.name] = release.generate_download_links(species.name)
        save_json(download_info, self.download_info_file)

    def download_fasta(self, release, species, file_type):
        download_info = load_json(self.download_info_file)
        if release not in download_info or species not in download_info[release]:
            raise ValueError(f"No download information for release {release} and species {species}")

        url = download_info[release][species][file_type]
        output_dir = f"downloads/release-{release}/{species}"
        ensure_directory(output_dir)
        
        subprocess.run(["wget", "-P", output_dir, url])
        print(f"Downloaded {file_type} FASTA for {species} (release {release})")