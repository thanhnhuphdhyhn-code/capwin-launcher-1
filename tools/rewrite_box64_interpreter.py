#!/usr/bin/env python3
"""Rewrite the packaged Box64 ELF interpreter for the CapWin Android package."""

from __future__ import annotations

import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

import zstandard


BOX64_RELATIVE_PATH = Path("usr/local/bin/box64")


def extract_archive(archive_path: Path, destination: Path) -> None:
    with archive_path.open("rb") as source, zstandard.ZstdDecompressor().stream_reader(source) as stream:
        with tarfile.open(fileobj=stream, mode="r|") as archive:
            for entry in archive:
                path = destination / entry.name.lstrip("./")
                if not path.resolve().is_relative_to(destination.resolve()):
                    raise RuntimeError(f"Unsafe archive path: {entry.name}")
                if entry.isdir():
                    path.mkdir(parents=True, exist_ok=True)
                elif entry.isreg():
                    path.parent.mkdir(parents=True, exist_ok=True)
                    source_file = archive.extractfile(entry)
                    if source_file is None:
                        raise RuntimeError(f"Unable to read {entry.name}")
                    path.write_bytes(source_file.read())
                    path.chmod(entry.mode)
                else:
                    raise RuntimeError(f"Unsupported archive entry: {entry.name}")


def repack_archive(source_dir: Path, archive_path: Path) -> None:
    with archive_path.open("wb") as target, zstandard.ZstdCompressor(level=8).stream_writer(target) as compressed:
        with tarfile.open(fileobj=compressed, mode="w|") as archive:
            for path in sorted(source_dir.rglob("*")):
                archive.add(path, arcname=f"./{path.relative_to(source_dir)}", recursive=False)


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: rewrite_box64_interpreter.py <archive.tzst> <interpreter-path>")
    archive_path = Path(sys.argv[1]).resolve()
    interpreter = sys.argv[2]
    with tempfile.TemporaryDirectory(prefix="capwin-box64-") as temp:
        root = Path(temp)
        extract_archive(archive_path, root)
        box64 = root / BOX64_RELATIVE_PATH
        if not box64.is_file():
            raise SystemExit(f"Box64 not found at {BOX64_RELATIVE_PATH}")
        subprocess.run(["patchelf", "--set-interpreter", interpreter, str(box64)], check=True)
        actual = subprocess.check_output(["patchelf", "--print-interpreter", str(box64)], text=True).strip()
        if actual != interpreter:
            raise SystemExit(f"Interpreter mismatch: {actual}")
        repack_archive(root, archive_path)
    print(f"Updated {archive_path.name} interpreter to {interpreter}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
