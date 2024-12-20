import shutil

from base_cloud_provider import CloudProvider


class OracleCloudProvider(CloudProvider):
    def detect(self):
        return "Oracle Cloud Solution" if shutil.which("oci") else None


CloudProvider.register("Oracle", OracleCloudProvider)
