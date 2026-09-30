---
name: cost-analysis
description: Analyze supplied cloud usage and pricing inputs to calculate transparent monthly costs and identify cost drivers.
---
# Cost Analysis

## Inputs
Accept structured usage quantity, unit price, billing periods per month, currency, and optional resource labels.

## Behavior
Validate numeric inputs and calculate monthly cost using the supplied values. Never invent provider pricing, discounts, taxes, or account inventory.

## Outputs
Return the monthly cost, currency, calculation expression, and enough source inputs to explain the result.

## Invalid Inputs
Reject missing, non-numeric, or negative values with a structured error.
