# Cloud Cost Optimization Agent

A portable OpenGAP v0.1.0 agent for deterministic cloud-cost analysis.

## Capabilities
- Calculate monthlyized cost from caller-supplied quantity, unit price, and billing period.
- Detect low-utilization signals from structured inputs.
- Produce rightsizing recommendations from explicit utilization thresholds and resource capacity data.

## Design
The core is framework-independent. Tool contracts live in `contracts/`, OpenGAP tool definitions live in `tools/`, implementations live in `core/`, and adapters translate external framework requests into the portable contract.

## Configuration
No provider credentials or production runtime configuration are embedded. `.env.example` documents optional runtime settings. Provider prices and account/resource data must be supplied by the caller or an authenticated external integration.

## Validation
Run:

```bash
pytest -q
python verification/audit.py
python verification/validate_manifest.py
```

If `opengap` is installed, additionally run `opengap validate`. This repository does not claim HiDevs verification until the external HiDevs validator returns that status.
