from .validation import require_number

def recommend_rightsizing(data: dict) -> dict:
    utilization = require_number(data, "utilization_percent", minimum=0)
    threshold = require_number(data, "rightsizing_threshold_percent", minimum=0)
    current_capacity = require_number(data, "current_capacity", minimum=0)
    target_capacity = require_number(data, "target_capacity", minimum=0)
    monthly_cost = require_number(data, "monthly_cost", minimum=0)
    if target_capacity > current_capacity:
        raise ValueError("target_capacity cannot exceed current_capacity for a rightsizing recommendation")
    if utilization < threshold and current_capacity > 0 and target_capacity < current_capacity:
        ratio = target_capacity / current_capacity
        estimated_monthly_cost = monthly_cost * ratio
        estimated_savings = monthly_cost - estimated_monthly_cost
        return {"recommendation": "consider_rightsizing", "estimated_monthly_cost": round(estimated_monthly_cost, 8), "estimated_monthly_savings": round(estimated_savings, 8), "basis": f"utilization {utilization}% < threshold {threshold}%"}
    return {"recommendation": "no_rightsizing_signal", "estimated_monthly_cost": monthly_cost, "estimated_monthly_savings": 0.0, "basis": "rightsizing threshold not met or target capacity is not smaller"}
