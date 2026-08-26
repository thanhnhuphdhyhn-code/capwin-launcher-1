#!/usr/bin/env python3
"""Migrate and verify JNI exports after the Java package changes to CapWin."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CPP_ROOT = ROOT / "app" / "app" / "src" / "main" / "cpp"
OLD = b"Java_com_winlator_"
NEW = b"Java_com_capwin_launcher_"
SOURCE_SUFFIXES = {".c", ".cc", ".cpp", ".h"}


def native_sources() -> list[Path]:
    return sorted(path for path in CPP_ROOT.rglob("*") if path.is_file() and path.suffix in SOURCE_SUFFIXES)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="rewrite stale Winlator JNI export prefixes")
    args = parser.parse_args()

    replacements = 0
    for path in native_sources():
        content = path.read_bytes()
        count = content.count(OLD)
        if not count:
            continue
        if not args.apply:
            print(f"STALE JNI PREFIX: {path.relative_to(ROOT)} ({count})")
            continue
        path.write_bytes(content.replace(OLD, NEW))
        replacements += count
        print(f"UPDATED: {path.relative_to(ROOT)} ({count})")

    remaining = []
    native_exports = 0
    for path in native_sources():
        content = path.read_bytes()
        count = content.count(OLD)
        if count:
            remaining.append(f"{path.relative_to(ROOT)} ({count})")
        native_exports += content.count(NEW)

    if remaining:
        print("ERROR: stale JNI exports remain:\n" + "\n".join(remaining))
        return 1
    if native_exports == 0:
        print("ERROR: no CapWin JNI exports were found")
        return 1
    print(f"OK: {native_exports} CapWin JNI exports verified; {replacements} export(s) updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
