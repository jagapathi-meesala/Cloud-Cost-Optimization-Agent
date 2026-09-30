"""Compatibility boundary for openai.sdk. No framework dependency is imported here."""
from .portable_adapter import PortableAdapter

class Adapter(PortableAdapter):
    framework = "openai_sdk"
