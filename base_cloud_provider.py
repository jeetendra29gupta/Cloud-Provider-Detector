from abc import ABC, abstractmethod


class CloudProvider(ABC):
    providers = {}

    @abstractmethod
    def detect(self):
        raise NotImplementedError("Subclasses must implement this method.")

    @classmethod
    def register(cls, provider_name, provider_class):
        cls.providers[provider_name] = provider_class
