#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json
import marshal
import re
import sys
import types
from pathlib import Path

PYC_HEADER_SIZE = 16
PRINTABLE_RE = re.compile(r"[A-Za-z\u4e00-\u9fff]")


def load_code(path: Path) -> types.CodeType:
    data = path.read_bytes()
    if len(data) <= PYC_HEADER_SIZE:
        raise ValueError(f"{path} is too small to be a valid .pyc file")
    return marshal.loads(data[PYC_HEADER_SIZE:])


def walk_code(
    code: types.CodeType,
    *,
    file_path: str,
    seen: set[int],
    qualname: str = "<module>",
) -> list[dict[str, str]]:
    if id(code) in seen:
        return []
    seen.add(id(code))

    items: list[dict[str, str]] = []
    for const in code.co_consts:
        if isinstance(const, str):
            value = const.strip()
            if len(value) >= 2 and PRINTABLE_RE.search(value):
                items.append(
                    {
                        "file": file_path,
                        "qualname": qualname,
                        "string": value,
                    }
                )
        elif isinstance(const, types.CodeType):
            nested = const.co_qualname or const.co_name or "<code>"
            items.extend(
                walk_code(
                    const,
                    file_path=file_path,
                    seen=seen,
                    qualname=nested,
                )
            )
    return items


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract likely user-facing string constants from Python 3.11 .pyc files."
    )
    parser.add_argument("paths", nargs="+", help="One or more .pyc files to inspect.")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of a plain-text list.",
    )
    args = parser.parse_args()

    results: list[dict[str, str]] = []
    for raw_path in args.paths:
        path = Path(raw_path)
        code = load_code(path)
        results.extend(walk_code(code, file_path=str(path), seen=set()))

    unique: list[dict[str, str]] = []
    seen_items: set[tuple[str, str, str]] = set()
    for item in results:
        key = (item["file"], item["qualname"], item["string"])
        if key in seen_items:
            continue
        seen_items.add(key)
        unique.append(item)

    if args.json:
        json.dump(unique, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0

    for item in unique:
        print(f"{item['file']}\t{item['qualname']}\t{item['string']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
