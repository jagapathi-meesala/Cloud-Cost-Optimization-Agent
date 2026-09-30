import pytest
from core.cost_calculator import calculate_cloud_cost
from core.waste_detector import detect_cost_waste
from core.rightsizing import recommend_rightsizing
from core.registry import ToolRegistry

def test_cost_calculation():
    assert calculate_cloud_cost({"quantity":10,"unit_price":2,"periods_per_month":1,"currency":"USD"})["monthly_cost"] == 20

def test_cost_rejects_negative():
    with pytest.raises(ValueError): calculate_cloud_cost({"quantity":-1,"unit_price":2,"periods_per_month":1,"currency":"USD"})

def test_waste_signal():
    result = detect_cost_waste({"utilization_percent":10,"low_utilization_threshold_percent":20,"monthly_cost":100})
    assert result["signals"][0]["type"] == "low_utilization"

def test_no_waste_signal():
    result = detect_cost_waste({"utilization_percent":30,"low_utilization_threshold_percent":20,"monthly_cost":100})
    assert result["signals"][0]["severity"] == "none"

def test_rightsizing():
    result = recommend_rightsizing({"utilization_percent":10,"rightsizing_threshold_percent":20,"current_capacity":10,"target_capacity":5,"monthly_cost":100})
    assert result["estimated_monthly_savings"] == 50

def test_rightsizing_no_signal():
    result = recommend_rightsizing({"utilization_percent":40,"rightsizing_threshold_percent":20,"current_capacity":10,"target_capacity":5,"monthly_cost":100})
    assert result["recommendation"] == "no_rightsizing_signal"

def test_registry():
    registry = ToolRegistry()
    assert registry.discover() == ["calculate-cloud-cost","detect-cost-waste","recommend-rightsizing"]
    assert registry.execute("calculate-cloud-cost", {"quantity":1,"unit_price":3,"periods_per_month":1,"currency":"USD"})["ok"]

def test_registry_unknown():
    registry = ToolRegistry()
    with pytest.raises(KeyError): registry.execute("unknown", {})

def test_registry_invalid_input():
    registry = ToolRegistry()
    result = registry.execute("calculate-cloud-cost", {"quantity":1})
    assert result["ok"] is False
