# Backup Drill Check

| | |
| --- | --- |
| Focus | recovery drills |
| Command | `backup-drill-check` |
| Inputs | text, JSON, JSONL, or CSV |
| Output | Markdown or JSON |

![Backup Drill Check cover](assets/readme-cover.svg)

Audit backup plans for restore proof, RPO, and RTO gaps. The repository is intentionally plain: a small command, a visible rule surface, and enough examples to make the behavior inspectable.

## Policy surface

| Rule | Level | Why it matters |
| --- | --- | --- |
| `restore-never-tested` | high | restore test is missing |
| `unknown-rpo` | medium | RPO is not defined |
| `missing-rto` | low | RTO is not defined |

## Local run

```bash
git clone https://github.com/mertefekurt/backup-drill-check.git
cd backup-drill-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
backup-drill-check examples/sample.txt
backup-drill-check examples/sample.txt --json
```

## Why the sample fails

`backup daily restore_test never rpo unknown rto missing` is intentionally shaped to hit the rules above, so it is useful as a quick smoke test after edits.
