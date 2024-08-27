import argparse
from src.services.release_service import ReleaseService
from src.services.species_service import SpeciesService
from src.services.download_service import DownloadService

def update_data():
    release_service = ReleaseService()
    species_service = SpeciesService()
    download_service = DownloadService()

    if release_service.update_available_releases():
        print("New release added")
    
    species_list = species_service.update_species_info()
    releases = release_service.get_all_releases()
    
    download_service.update_download_info(releases, species_list)
    print("Download info updated")

def download_fasta(release, species, file_type):
    download_service = DownloadService()
    download_service.download_fasta(release, species, file_type)

def main():
    parser = argparse.ArgumentParser(description="Ensembl data management")
    parser.add_argument("--update", action="store_true", help="Update all data")
    parser.add_argument("--download", nargs=3, metavar=("RELEASE", "SPECIES", "TYPE"), help="Download FASTA file")
    
    args = parser.parse_args()

    if args.update:
        update_data()
    elif args.download:
        download_fasta(*args.download)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()