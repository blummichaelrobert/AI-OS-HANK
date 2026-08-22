"""
AI OS V3 — Shared Captain Dependency
fetch_decode: gzip/binary-safe URL fetch, decode-only. No parsing.
Importable only. No CLI. Called by Captains via bash, not invoked by HANK directly.
"""

import gzip

import requests


def fetch_decode(url: str, timeout: int = 15) -> dict:
    """
    Fetch a URL and return decoded text, handling gzip/compressed bodies that
    CoWork's native WebFetch cannot decode.

    Returns:
    {
      "url": str,
      "success": bool,
      "status_code": int | None,
      "content_type": str | None,
      "decoded_text": str | None,
      "error": str | None   # "fetch_failed" | "decode_failed" | None
    }
    """
    result = {
        "url": url,
        "success": False,
        "status_code": None,
        "content_type": None,
        "decoded_text": None,
        "error": None,
    }

    try:
        response = requests.get(url, timeout=timeout)
    except requests.exceptions.RequestException:
        result["error"] = "fetch_failed"
        return result

    result["status_code"] = response.status_code
    result["content_type"] = response.headers.get("Content-Type")

    if not response.ok:
        result["error"] = "fetch_failed"
        return result

    raw = response.content

    # gzip magic bytes present but Content-Encoding wasn't set/honored, so
    # requests didn't auto-decompress — decompress manually before decoding.
    if raw[:2] == b"\x1f\x8b":
        try:
            result["decoded_text"] = gzip.decompress(raw).decode("utf-8")
            result["success"] = True
            return result
        except Exception:
            result["error"] = "decode_failed"
            return result

    try:
        encoding = response.encoding or response.apparent_encoding or "utf-8"
        result["decoded_text"] = raw.decode(encoding)
        result["success"] = True
        return result
    except (UnicodeDecodeError, LookupError, TypeError):
        result["error"] = "decode_failed"
        return result
