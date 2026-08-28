from pathlib import Path

ROOT = Path(__file__).resolve().parent
required = [
    "README.md",
    "LICENSE",
    "paper/AI_Assisted_Research_Paper.pdf",
    "citation-audit/Citation_Integrity_Audit.pdf",
    "references/references.md",
    "datasets/datasets.md",
    "tools/tools.md",
    "implementations/github-repositories.md",
    "tutorials/tutorials.md",
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    raise SystemExit("Missing required files:\n" + "\n".join(missing))

text = (ROOT / "references/references.md").read_text(encoding="utf-8")
count = sum(1 for line in text.splitlines() if line.startswith(tuple(f"{i}. " for i in range(1, 100))))
if count < 20:
    raise SystemExit(f"Expected >=20 curated papers, found {count}")

print(f"Repository validation passed: {count} curated papers")
