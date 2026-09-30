"""Compatibility boundary for lyzr. No framework dependency is imported here."""
from .portable_adapter import PortableAdapter

class Adapter(PortableAdapter):
    framework = "lyzr"
