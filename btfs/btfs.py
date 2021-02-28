import json
import urllib


class BTFS:

    default_path_btfs = ".btfs"
    default_path_root = f"~/{default_path_btfs}"
    default_api_file = "api"
    default_api_version = "v1"
    environment_directory = "BTFS_PATH"

    def __init__(self, host_name, port):
        self.btfs_hostname = host_name
        self.btfs_port = port
        self.btfs_url_api = f"http://{self.btfs_hostname}:{btfs_port}/{default_api_file}/{default_api_version}/"

    def get_response(self, urllib_obj):
        with urllib.request.urlopen(urllib_obj) as req:
            response = json.read(req.read())
            return response


class BTFSConfiguration(BTFS):

    btfs_config_url = f"{self.btfs_url_api}config/"

    def __init__(self, host_name, port):
        super.__init__(host_name, port)

    def apply_profile(self, profile_name):
        profile_type = f"{btfs_config_url}/profile/apply?arg={profile_name}"
        urllib_obj = urllib.request.Request(
            url=f"{profile_type}", method="POST")

        return self.get_response(urllib_obj)


class BTFSStorage(BTFS):

    btfs_storage_url = f"{self.btfs_url_api}storage/"

    def __init__(self, host_name, port):
        super.__init__(host_name, port)

    def sync_storage_host(self):
        urllib_obj = f"{self.btfs_storage_url}"
        return self.get_response(urllib_obj)
