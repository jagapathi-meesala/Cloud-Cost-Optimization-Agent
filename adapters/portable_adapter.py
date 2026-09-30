from core.registry import ToolRegistry

class PortableAdapter:
    """Framework-neutral invocation boundary."""
    def __init__(self, registry=None):
        self.registry = registry or ToolRegistry()
    def invoke(self, tool_name: str, arguments: dict):
        return self.registry.execute(tool_name, arguments)
