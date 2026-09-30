# Rules

1. Reject missing, non-numeric, negative, or dimensionally inconsistent cost inputs.
2. Calculate estimated monthly cost as quantity × unit price × billing periods supplied by the caller.
3. Never assume a provider, region, currency, discount, tax, or commitment price when it is not supplied.
4. Flag utilization below the configured low-utilization threshold as a waste signal when that threshold is part of the input.
5. Recommend rightsizing only when utilization evidence meets the explicit rule thresholds.
6. Savings estimates are calculations from supplied prices and quantities, not guarantees.
7. Never execute infrastructure changes.
8. Never log or persist credentials or secret values.
