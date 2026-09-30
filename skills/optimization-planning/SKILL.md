---
name: optimization-planning
description: Identify deterministic cloud waste signals and conservative rightsizing opportunities from supplied utilization and capacity data.
---
# Optimization Planning

## Inputs
Accept utilization percentages, explicit thresholds, current and target capacity, and caller-supplied monthly cost.

## Behavior
Compare utilization against the supplied threshold and calculate an estimated cost change only when the target capacity is smaller and the rule is satisfied.

## Outputs
Return signals, recommendations, estimated monthly savings, and the exact rule basis.

## Limitations
Recommendations are advisory. They do not account for provider-specific service constraints unless those constraints are explicitly supplied.
