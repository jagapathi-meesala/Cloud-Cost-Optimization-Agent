from .validation import require_number

def calculate_cloud_cost(data: dict) -> dict:
    quantity = require_number(data, "quantity", minimum=0)
    unit_price = require_number(data, "unit_price", minimum=0)
    periods_per_month = require_number(data, "periods_per_month", minimum=0)
    currency = data.get("currency")
    if not isinstance(currency, str) or not currency.strip():
        raise ValueError("currency must be a non-empty string")
    cost = quantity * unit_price * periods_per_month
    return {
        "monthly_cost": round(cost, 8),
        "currency": currency,
        "calculation": "quantity * unit_price * periods_per_month",
    }
