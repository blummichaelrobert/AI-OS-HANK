"""
AI OS V3 — Validator Engine
Importable only. No CLI. Invoked by HANK at Meridian output boundaries.
"""

import json
import re
import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Module-level constants
# ---------------------------------------------------------------------------

_SESSION_LOG_PATH = (
    Path("/tmp/telemetry")
    / f"validation_{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.jsonl"
)

_BLOCK_RE = re.compile(
    r"<!-- AIOS-VALIDATION:START -->(.*?)<!-- AIOS-VALIDATION:END -->",
    re.DOTALL,
)
_FENCE_RE = re.compile(r"```json\s*([\s\S]*?)\s*```")

_JSON_TYPE_MAP = {
    "string": str,
    "object": dict,
    "array": list,
    "null": type(None),
}

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def validate(captain_md_path: str, output: dict) -> dict:
    schema, error_verdict = _load_schema(captain_md_path)
    if error_verdict:
        result = {
            "captain": Path(captain_md_path).stem,
            "verdict": error_verdict,
            "deltas": [],
        }
        _log(result, output)
        return result

    captain = schema.get("captain", Path(captain_md_path).stem)
    deltas = []

    _check_required(schema, output, deltas)
    _check_types(schema, output, deltas)
    _check_constants(schema, output, deltas)
    _check_conditional(schema, output, deltas)

    verdict = "pass" if not deltas else "output_failed"
    result = {"captain": captain, "verdict": verdict, "deltas": deltas}
    _log(result, output)
    return result

# ---------------------------------------------------------------------------
# Schema loading
# ---------------------------------------------------------------------------

def _load_schema(path: str):
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError:
        return None, "schema_missing"

    block_match = _BLOCK_RE.search(text)
    if not block_match:
        return None, "schema_missing"

    fence_match = _FENCE_RE.search(block_match.group(1))
    if not fence_match:
        return None, "schema_malformed"

    try:
        schema = json.loads(fence_match.group(1))
    except json.JSONDecodeError:
        return None, "schema_malformed"

    return schema, None

# ---------------------------------------------------------------------------
# Validation checks
# ---------------------------------------------------------------------------

def _check_required(schema, output, deltas):
    for field in schema.get("required", []):
        if field not in output or output[field] is None:
            deltas.append({"field": field, "reason": "required field missing or null"})


def _check_types(schema, output, deltas):
    for field, expected_type in schema.get("types", {}).items():
        if field not in output or output[field] is None:
            continue
        if not _matches_type(output[field], expected_type):
            deltas.append({
                "field": field,
                "reason": f"expected type '{expected_type}', got '{type(output[field]).__name__}'",
            })


def _check_constants(schema, output, deltas):
    for field, expected in schema.get("constants", {}).items():
        if field not in output:
            deltas.append({"field": field, "reason": f"constant field missing (expected {expected!r})"})
        elif output[field] != expected:
            deltas.append({
                "field": field,
                "reason": f"expected constant {expected!r}, got {output[field]!r}",
            })


def _check_conditional(schema, output, deltas):
    for rule in schema.get("conditional", []):
        when = rule.get("when", {})
        require_non_null = rule.get("require_non_null", [])
        if all(output.get(k) == v for k, v in when.items()):
            for field in require_non_null:
                if field not in output or output[field] is None:
                    condition = ", ".join(f"{k}={v!r}" for k, v in when.items())
                    deltas.append({
                        "field": field,
                        "reason": f"conditional requirement not met: must be non-null when {condition}",
                    })

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _matches_type(value, expected_type: str) -> bool:
    if expected_type == "boolean":
        return isinstance(value, bool)
    if expected_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    py_type = _JSON_TYPE_MAP.get(expected_type)
    if py_type is None:
        return True
    return isinstance(value, py_type)


def _log(result: dict, output: dict) -> None:
    try:
        _SESSION_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        entry = {
            "captain": result["captain"],
            "invoked_by": (output or {}).get("invoked_by", "unknown"),
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "verdict": result["verdict"],
            "deltas": result["deltas"],
        }
        with _SESSION_LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception:
        pass
