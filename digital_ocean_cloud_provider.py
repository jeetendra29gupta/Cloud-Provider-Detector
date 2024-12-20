import shutil

from base_cloud_provider import CloudProvider


class DigitalOceanCloudProvider(CloudProvider):
    def detect(self):
        return "DigitalOcean Cloud Solution" if shutil.which("doctl") else None



CloudProvider.register("Digital Ocean", DigitalOceanCloudProvider)
