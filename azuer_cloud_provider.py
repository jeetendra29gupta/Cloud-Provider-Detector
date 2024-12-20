import shutil

from base_cloud_provider import CloudProvider


class AzureCloudProvider(CloudProvider):
    def detect(self):
        return "Azure Cloud Solution" if shutil.which("az") else None


CloudProvider.register("Azure", AzureCloudProvider)
