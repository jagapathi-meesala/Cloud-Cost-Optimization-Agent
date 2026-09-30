from numbers import Real

def require_number(data: dict, key: str, *, minimum: float | None = None) -> float:
    if key not in data or isinstance(data[key], bool) or not isinstance(data[key], Real):
        raise ValueError(f"{key} must be a number")
    value = float(data[key])
    if minimum is not None and value < minimum:
        raise ValueError(f"{key} must be >= {minimum}")
    return value
