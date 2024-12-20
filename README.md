# Cloud Provider Detector

## Overview

The **Cloud Provider Detector** is a Python tool designed to detect which cloud provider a system is using by checking for the presence of their respective command-line interface (CLI) tools. It supports multiple cloud providers, including AWS, Azure, Alibaba Cloud, and others. This tool helps in identifying the cloud environment based on the available CLI tools in the system's `PATH`.

The project is designed to adhere to the **Open/Closed Principle (OCP)**, one of the SOLID design principles, making it **open for extension** and **closed for modification**. Additionally, **Dependency Injection** is used to ensure flexibility and testability of the components.

## Supported Cloud Providers

- **AWS**: Detects the presence of the AWS CLI (`aws`).
- **Azure**: Detects the presence of the Azure CLI (`az`).
- **Alibaba Cloud**: Detects the presence of the Alibaba Cloud CLI (`aliyun`).
- **Google Cloud**: Detects the presence of the Google Cloud CLI (`gcloud`).
- **IBM Cloud**: Detects the presence of the IBM Cloud CLI (`ibmcloud`).
- **Oracle Cloud**: Detects the presence of the Oracle Cloud CLI (`oci`).
- **DigitalOcean**: Detects the presence of the DigitalOcean CLI (`doctl`).

## Features

- **Extensible**: Easily add support for new cloud providers by creating new classes that inherit from the base `CloudProvider` class.
- **Cross-Platform**: Works across different operating systems as long as the respective CLI tools are in the system's `PATH`.
- **Command-Line Detection**: Uses the presence of cloud CLI tools to detect the cloud provider.
- **Open/Closed Principle (OCP)**: The design is open for extension but closed for modification. New cloud providers can be added without changing existing code.
- **Dependency Injection**: The system allows the injection of dependencies, promoting flexibility and testability of components.

## Installation

To install and use the Cloud Provider Detector, clone the repository and run the code.

### Prerequisites

Ensure that the following CLI tools are installed on your system (if you're testing with specific cloud providers):
- AWS CLI (`aws`)
- Azure CLI (`az`)
- Alibaba CLI (`aliyun`)
- Google Cloud SDK (`gcloud`)
- IBM Cloud CLI (`ibmcloud`)
- Oracle Cloud CLI (`oci`)
- DigitalOcean CLI (`doctl`)

## Usage

### Example: Detect Cloud Provider

```python
from cloud_provider_manager import CloudProviderManager

# Create an instance of CloudProviderManager
manager = CloudProviderManager()

# Detect the cloud provider
cloud_provider = manager.detect_cloud_provider()
print(f"Cloud Provider: {cloud_provider}")
```

This will print the detected cloud provider based on the available CLI tool.

### Example Output

If `aws` CLI is found, it will print:
```
Cloud Provider: AWS Cloud Solution
```

If none of the CLI tools are found, it will print:
```
Cloud Provider: Unknown
```

## Design Principles

### Open/Closed Principle (OCP)

The **Open/Closed Principle** is part of the SOLID principles of object-oriented design. According to OCP, a class should be **open for extension** but **closed for modification**. This means that the design of the system should allow new functionality (e.g., new cloud providers) to be added without changing the existing code.

#### How OCP is Applied

- The **CloudProvider** class is abstract, and subclasses must implement the `detect()` method.
- New cloud providers are added by creating new subclasses of `CloudProvider` and registering them with the `CloudProvider` class using the `register()` method.
- This approach ensures that no modification is needed to the existing codebase when adding new cloud providers. You simply create new provider classes and register them.

#### Example: Adding a New Cloud Provider

```python
import shutil
from base_cloud_provider import CloudProvider

class ExampleCloudProvider(CloudProvider):
    def detect(self):
        return "Example Cloud Solution" if shutil.which("example-cli") else None

# Register the provider
CloudProvider.register("ExampleCloud", ExampleCloudProvider)
```

No changes are needed to the `CloudProviderManager` or any other parts of the code to add new providers.

### Dependency Injection

**Dependency Injection** is a design pattern used to implement Inversion of Control (IoC), which allows for better flexibility, maintainability, and testability of your code. It decouples the creation of dependent objects from the classes that use them.

#### How Dependency Injection is Applied

- In the **CloudProviderManager** class, we could inject the cloud provider classes instead of directly instantiating them. This makes the manager more flexible and easier to test.

#### Example with Dependency Injection

Instead of directly appending providers inside `CloudProviderManager`, we could inject the list of providers during initialization:

```python
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
```

This allows you to easily inject custom providers, which can be especially useful for testing.

```python
# Example Usage with Dependency Injection
custom_providers = [AwsCloudProvider, AzureCloudProvider, ExampleCloudProvider]
manager = CloudProviderManager(providers=custom_providers)

cloud_provider = manager.detect_cloud_provider()
print(f"Cloud Provider: {cloud_provider}")
```

In this case, `CloudProviderManager` is now flexible and decoupled from specific provider implementations. It can easily be adapted to different configurations of providers, whether for testing or production.

## Extending with New Cloud Providers

To add a new cloud provider, follow these steps:

1. **Create a new class** that inherits from the `CloudProvider` base class.
2. **Override the `detect()` method** to check for the specific cloud provider’s CLI tool.
3. **Register the new provider** with `CloudProvider.register()`.

Example of adding a new cloud provider (for example, **Example Cloud**):

```python
import shutil
from base_cloud_provider import CloudProvider

class ExampleCloudProvider(CloudProvider):
    def detect(self):
        return "Example Cloud Solution" if shutil.which("example-cli") else None

# Register the provider
CloudProvider.register("ExampleCloud", ExampleCloudProvider)
```

### Steps:
1. Create a new file for the cloud provider (e.g., `example_cloud_provider.py`).
2. Implement the detection logic similar to the other providers.
3. Add the provider registration in the `CloudProvider.register()` method.

