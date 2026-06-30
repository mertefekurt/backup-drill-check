# backup-drill-check

**Review Workflow.** Audit backup plans for restore proof, RPO, and RTO gaps.

## When To Run

Backups are only useful when restore is tested. This CLI reviews backup plans for missing recovery targets and stale restore drills.

## How It Scores

`backup-drill-check` accepts backup policy text or disaster recovery notes in text, JSON, JSONL, or CSV form.

## JSON Mode

```bash
python -m pip install -e ".[dev]"
backup-drill-check examples/sample.txt
backup-drill-check examples/sample.txt --json --fail-on medium
```

## CI Usage

| Rule | Severity | Meaning |
|---|---:|---|
| `restore-never-tested` | high | restore test is missing |
| `unknown-rpo` | medium | RPO is not defined |
| `missing-rto` | low | RTO is not defined |

## License

```bash
ruff check .
pytest
python -m backup_drill_check --help
```

License: MIT

### Example Input

```text
backup daily restore_test never rpo unknown rto missing
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the backup-drill-check policy surface explicit.
