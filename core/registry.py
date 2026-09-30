from .cost_calculator import calculate_cloud_cost
from .waste_detector import detect_cost_waste
from .rightsizing import recommend_rightsizing

class ToolRegistry:
    def __init__(self):
        self._tools = {
            "calculate-cloud-cost": calculate_cloud_cost,
            "detect-cost-waste": detect_cost_waste,
            "recommend-rightsizing": recommend_rightsizing,
        }
    def discover(self) -> list[str]:
        return sorted(self._tools)
    def register(self, name, function):
        if not isinstance(name, str) or not name:
            raise ValueError("tool name must be non-empty")
        if not callable(function):
            raise TypeError("tool must be callable")
        self._tools[name] = function
    def execute(self, name, payload):
        if name not in self._tools:
            raise KeyError(f"unknown tool: {name}")
        if not isinstance(payload, dict):
            raise TypeError("tool input must be an object")
        try:
            return {"ok": True, "tool": name, "result": self._tools[name](payload)}
        except (ValueError, TypeError) as exc:
            return {"ok": False, "tool": name, "error": str(exc)}
