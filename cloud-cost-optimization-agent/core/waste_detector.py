from .validation import require_number

def detect_cost_waste(data: dict) -> dict:
    utilization = require_number(data, "utilization_percent", minimum=0)
    threshold = require_number(data, "low_utilization_threshold_percent", minimum=0)
    monthly_cost = require_number(data, "monthly_cost", minimum=0)
    signals = []
    if utilization < threshold:
        signals.append({"type": "low_utilization", "severity": "review", "reason": f"utilization {utilization}% is below threshold {threshold}%"})
    if not signals:
        signals.append({"type": "no_low_utilization_signal", "severity": "none", "reason": "utilization is at or above the supplied threshold"})
    return {"monthly_cost": monthly_cost, "utilization_percent": utilization, "signals": signals}
