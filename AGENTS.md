# Agents

## Architecture
The agent consists of a framework-independent core, typed contracts, a dynamic registry, deterministic Python tools, documentation skills, and compatibility adapters.

## Development Rules
Keep runtime configuration in environment variables. Keep provider-specific prices and account data in explicit inputs or external integrations; never embed production secrets or assumed account values.

## Tool Conventions
Each tool has a YAML contract and Python implementation. Tool names are kebab-case and registry keys match their manifest names.

## Testing Rules
Run `pytest -q` after changes. Also run the verification scripts and schema validation before claiming local readiness.

## Portability
Core logic must not import OpenAI, CrewAI, Claude, Lyzr, or another framework. Adapters may translate framework-specific calls into the portable tool contract.
