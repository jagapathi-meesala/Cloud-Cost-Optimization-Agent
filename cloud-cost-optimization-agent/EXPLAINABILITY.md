# Explainability

## Inputs and Data Sources
The agent accepts structured cloud usage, pricing, utilization, capacity, threshold, and currency inputs supplied by the caller. Data sources are limited to those inputs or explicitly connected external systems; the agent does not invent provider prices or account inventory.

## Decision and Reasoning
The agent validates inputs and applies deterministic arithmetic and threshold rules to calculate costs, detect low-utilization signals, and estimate rightsizing effects. Each recommendation reports the supplied values and rule basis so a reviewer can reproduce the calculation.

## Limits and Constraints
The agent cannot verify cloud-account state, provider-specific pricing, contractual discounts, taxes, or service dependencies unless those data are explicitly supplied or connected. Recommendations are advisory and do not authorize infrastructure changes.

## Agent Purpose
The agent converts cloud cost and utilization data into transparent analysis that can support human FinOps decisions.

## Input Mechanisms
Inputs arrive through the portable tool contract as structured objects. Each tool validates required fields, numeric ranges, and required strings before execution.

## Decision Mechanisms
Cost calculation uses `quantity * unit_price * periods_per_month`. Waste detection compares utilization with the caller-supplied low-utilization threshold, while rightsizing compares utilization with its threshold and only estimates savings when target capacity is smaller than current capacity.

## Execution Limits
The agent performs calculations and recommendations only. It does not provision, resize, delete, stop, or modify cloud resources.

## Output Contract
Tool responses contain either `ok: true` with a structured result or `ok: false` with an error message. Calculated outputs preserve the supplied currency and report the calculation or decision basis.

## Complete Execution Lifecycle
A request enters through an adapter, reaches the portable registry, is validated by the selected tool, is processed by deterministic core logic, and returns a structured result to the caller. No framework-specific runtime is required by the core.

## Tool-by-tool Behavior
`calculate-cloud-cost` computes monthly cost; `detect-cost-waste` identifies low-utilization signals; and `recommend-rightsizing` estimates a rightsizing opportunity when its explicit rule is satisfied.

### Input Requirements
Each tool requires the fields declared in its corresponding YAML contract. Values outside the documented numeric constraints are rejected.

### Failure Handling
Validation failures are returned as structured errors and do not trigger infrastructure changes. Unknown tool names are rejected by the registry.

### Rules Applied
Only rules documented in `RULES.md` and implemented in the core modules are applied. Provider-specific assumptions are excluded unless supplied as data.

### Constraints
Savings estimates are mathematical estimates based on supplied inputs and should not be treated as guaranteed financial outcomes. Real-world constraints such as licensing, redundancy, performance requirements, and contractual pricing require additional evidence.

### Expected Outputs
A successful tool call returns structured fields appropriate to the tool and includes a calculation or basis for the result. An unsuccessful call identifies the validation or execution error.

### Worked Example
For quantity 10, unit price 2, periods per month 1, and currency USD, the cost calculation returns a monthly cost of 20 USD. If utilization is 15%, the low-utilization threshold is 20%, current capacity is 10 units, target capacity is 5 units, and monthly cost is 20 USD, the rightsizing estimate is 10 USD monthly savings under the stated proportional-capacity rule.

### Explainability of Calculated Results
Every monetary result is derived from explicit input values using arithmetic that can be independently reproduced. Rightsizing savings are estimated as current monthly cost minus monthly cost multiplied by target capacity divided by current capacity.

### Provenance
The provenance of a result is the structured input payload and the versioned tool implementation that processed it. External provider data must be supplied with its own source metadata when provenance beyond caller input is required.
