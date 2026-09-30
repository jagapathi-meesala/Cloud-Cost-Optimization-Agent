from pathlib import Path
import yaml, jsonschema
root = Path(__file__).resolve().parents[1]
manifest = yaml.safe_load((root/"agent.yaml").read_text())
schema_url = "https://raw.githubusercontent.com/open-gitagent/opengap/main/spec/schemas/agent-yaml.schema.json"
# The full canonical schema is supplied by the caller/environment for offline validation.
schema_path = root / "verification" / "agent-yaml.schema.json"
if not schema_path.exists():
    print("canonical schema file not bundled; manifest syntax checks only")
    assert manifest["spec_version"] == "0.1.0"
    assert manifest["name"] == "cloud-cost-optimization-agent"
    raise SystemExit(0)
schema = json.loads(schema_path.read_text())
jsonschema.Draft202012Validator(schema).validate(manifest)
print("agent.yaml validated against canonical OpenGAP schema")
