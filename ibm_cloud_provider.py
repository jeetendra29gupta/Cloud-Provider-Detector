import shutil

from base_cloud_provider import CloudProvider


class IbmCloudProvider(CloudProvider):
    def detect(self):
        return "IBM Cloud Solution" if shutil.which("ibmcloud") else None


CloudProvider.register("IBM", IbmCloudProvider)
