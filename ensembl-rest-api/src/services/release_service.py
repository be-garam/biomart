from src.utils.api_utils import get_json_from_api
from src.utils.file_utils import load_json, save_json
from src.models.ensembl_release import EnsemblRelease

class ReleaseService:
    def __init__(self):
        self.releases_file = "config/available_releases.json"

    def get_latest_release(self):
        data = get_json_from_api("info/data")
        return max(release['version'] for release in data['releases'])

    def update_available_releases(self):
        latest_release = self.get_latest_release()
        releases = load_json(self.releases_file) if os.path.exists(self.releases_file) else []
        
        if latest_release not in releases:
            releases.append(latest_release)
            releases.sort(reverse=True)
            save_json(releases, self.releases_file)
            return True
        return False

    def get_all_releases(self):
        return [EnsemblRelease(version) for version in load_json(self.releases_file)]