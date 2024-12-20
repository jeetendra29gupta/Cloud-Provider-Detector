import shutil

from base_cloud_provider import CloudProvider


class AwsCloudProvider(CloudProvider):
    def detect(self):
        return "AWS Cloud Solution" if shutil.which("aws") else None


CloudProvider.register("AWS", AwsCloudProvider)
