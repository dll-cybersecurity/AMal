#!/usr/bin/env python3
"""
Prüft alle Indikatoren in data/indicators.json per HTTP-Request
und aktualisiert das "status"-Feld (online/offline).

Aufruf: python check_indicators.py
Erwartet: data/indicators.json relativ zum Repo-Root
"""

import json
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

INDICATORS_FILE = Path("data/indicators.json")
TIMEOUT_SECONDS = 8
USER_AGENT = "AMal-Indicator-Checker/1.0 (+https://github.com/dll-cybersecurity/AMal)"


def check_url(url: str) -> bool:
    """Gibt True zurück, wenn der Host unter der URL antwortet (egal welcher Statuscode)."""
    req = Request(url, headers={"User-Agent": USER_AGENT}, method="GET")
    try:
        with urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            # Jede Antwort (auch 403/404/500) heißt: der Host lebt.
            return resp.status is not None
    except HTTPError:
        # Server hat geantwortet, nur mit Fehlercode -> Host ist online
        return True
    except (URLError, TimeoutError, ConnectionError, OSError):
        # Keine Verbindung möglich -> vermutlich offline
        return False


def check_entry(entry: dict) -> bool:
    """Ein Eintrag gilt als 'online', wenn MINDESTENS EINER seiner Indikator-URLs antwortet."""
    for url in entry.get("indicator", []):
        if url.startswith("http://") or url.startswith("https://"):
            if check_url(url):
                return True
    return False


def main() -> int:
    if not INDICATORS_FILE.exists():
        print(f"Fehler: {INDICATORS_FILE} nicht gefunden.", file=sys.stderr)
        return 1

    data = json.loads(INDICATORS_FILE.read_text(encoding="utf-8"))
    changed = False

    for entry in data:
        old_status = entry.get("status")
        is_online = check_entry(entry)
        new_status = "online" if is_online else "offline"

        if new_status != old_status:
            print(f"[{entry.get('id')}] {old_status} -> {new_status}")
            entry["status"] = new_status
            changed = True
        else:
            print(f"[{entry.get('id')}] unverändert ({old_status})")

    if changed:
        INDICATORS_FILE.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print("indicators.json aktualisiert.")
    else:
        print("Keine Änderungen nötig.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
