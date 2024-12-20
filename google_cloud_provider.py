import shutil

from base_cloud_provider import CloudProvider


class GoogleCloudProvider(CloudProvider):
    def detect(self):
        return "Google Cloud Solution" if shutil.which("gcloud") else None


CloudProvider.register("Google", GoogleCloudProvider)
