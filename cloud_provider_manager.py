from alibaba_cloud_provider import AlibabaCloudProvider  # noqa: F401
from aws_cloud_provider import AwsCloudProvider  # noqa: F401
from azuer_cloud_provider import AzureCloudProvider  # noqa: F401
from base_cloud_provider import CloudProvider
from digital_ocean_cloud_provider import DigitalOceanCloudProvider  # noqa: F401
from google_cloud_provider import GoogleCloudProvider  # noqa: F401
from ibm_cloud_provider import IbmCloudProvider  # noqa: F401
from oracle_cloud_provider import OracleCloudProvider  # noqa: F401


class CloudProviderManager:
    def __init__(self, providers=None):
        # Use injected providers list, or default to an empty list
        self.providers = providers or list(CloudProvider.providers.values())

    def detect_cloud_provider(self):
        for provider in self.providers:
            result = provider().detect()
            if result:
                return result
        return "Unknown"


# Example Usage
if __name__ == "__main__":
    manager = CloudProviderManager()

    cloud_provider = manager.detect_cloud_provider()
    print(f"Cloud Provider: {cloud_provider}")

    # Example Usage with Dependency Injection
    # custom_providers = [AwsCloudProvider, AzureCloudProvider, ExampleCloudProvider]
    # manager = CloudProviderManager(providers=custom_providers)

    # cloud_provider = manager.detect_cloud_provider()
    # print(f"Cloud Provider: {cloud_provider}")