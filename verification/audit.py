from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
required = ["agent.yaml","SOUL.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md",".env.example"]
missing = [p for p in required if not (root/p).exists()]
assert not missing, f"missing: {missing}"
text = (root/"EXPLAINABILITY.md").read_text()
for h in ["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]:
    assert h in text, f"missing heading: {h}"
for h in ["## Inputs","## Decision","## Limits"]:
    assert not re.search(r"^" + re.escape(h) + r"\s*$", text, flags=re.M), f"conflicting heading: {h}"
sections = re.split(r"^## ", text, flags=re.M)
for required_heading in ["Inputs and Data Sources","Decision and Reasoning","Limits and Constraints"]:
    section = next(s for s in sections if s.startswith(required_heading))
    body = section.split("\n",1)[1] if "\n" in section else ""
    sentences = [x for x in re.split(r"(?<=[.!?])\s+", body.strip()) if x]
    assert len(sentences) >= 2, f"not enough sentences under {required_heading}"
print("documentation structural audit passed")
