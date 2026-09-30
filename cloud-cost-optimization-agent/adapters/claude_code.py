"""Compatibility boundary for claude.code. No framework dependency is imported here."""
from .portable_adapter import PortableAdapter

class Adapter(PortableAdapter):
    framework = "claude_code"
