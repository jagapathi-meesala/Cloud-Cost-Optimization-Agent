"""Compatibility boundary for crewai. No framework dependency is imported here."""
from .portable_adapter import PortableAdapter

class Adapter(PortableAdapter):
    framework = "crewai"
