from __future__ import annotations

from backup_drill_check.models import Rule

PROJECT_NAME = 'backup-drill-check'
SUMMARY = 'Audit backup plans for restore proof, RPO, and RTO gaps.'
SAMPLE_RISK = 'backup daily restore_test never rpo unknown rto missing'
SAMPLE_CLEAN = 'backup hourly restore_test 2026-06-01 rpo 15m rto 1h'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='restore-never-tested',
        severity='high',
        pattern='\\brestore(_test)?\\s*(never|none|missing)\\b',
        message='restore test is missing',
        recommendation='Schedule and record a restore drill.',
    ),
    Rule(
        code='unknown-rpo',
        severity='medium',
        pattern='\\brpo\\s*(unknown|missing|none)\\b',
        message='RPO is not defined',
        recommendation='Define maximum acceptable data loss.',
    ),
    Rule(
        code='missing-rto',
        severity='low',
        pattern='\\brto\\s*(missing|unknown|none)\\b',
        message='RTO is not defined',
        recommendation='Define target recovery time and owner.',
    ),
)
