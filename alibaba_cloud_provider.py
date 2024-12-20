import shutil

from base_cloud_provider import CloudProvider


class AlibabaCloudProvider(CloudProvider):
    def detect(self):
        return "Alibaba Cloud Solution" if shutil.which("aliyun") else None


CloudProvider.register("Alibaba", AlibabaCloudProvider)
