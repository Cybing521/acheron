#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json
import marshal
import types
import re
from pathlib import Path

PYC_HEADER_SIZE = 16
WHITESPACE_RE = re.compile(r"^(\s*)(.*?)(\s*)$", re.DOTALL)


def load_mapping(path: Path) -> dict[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Mapping file must be a JSON object")
    return {str(k): str(v) for k, v in data.items()}


def patch_code(
    code: types.CodeType,
    mapping: dict[str, str],
    counter: dict[str, int],
) -> types.CodeType:
    new_consts = []
    changed = False

    for const in code.co_consts:
        if isinstance(const, str):
            replacement = mapping.get(const)
            if replacement is None:
                match = WHITESPACE_RE.match(const)
                if match is not None:
                    leading, middle, trailing = match.groups()
                    mapped_middle = mapping.get(middle)
                    if mapped_middle is not None:
                        replacement = f"{leading}{mapped_middle}{trailing}"
            if replacement is not None:
                new_consts.append(replacement)
                counter["replacements"] += 1
                changed = True
            else:
                new_consts.append(const)
        elif isinstance(const, types.CodeType):
            patched = patch_code(const, mapping, counter)
            new_consts.append(patched)
            changed = changed or (patched is not const)
        else:
            new_consts.append(const)

    if not changed:
        return code
    return code.replace(co_consts=tuple(new_consts))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Patch string constants inside Python 3.11 .pyc files."
    )
    parser.add_argument("input", help="Source .pyc file")
    parser.add_argument("output", help="Patched .pyc output path")
    parser.add_argument(
        "--mapping",
        required=True,
        help="JSON file mapping English strings to Chinese strings",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    mapping = load_mapping(Path(args.mapping))

    data = input_path.read_bytes()
    header = data[:PYC_HEADER_SIZE]
    code = marshal.loads(data[PYC_HEADER_SIZE:])

    counter = {"replacements": 0}
    patched = patch_code(code, mapping, counter)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(header + marshal.dumps(patched))
    print(
        f"patched={counter['replacements']} input={input_path} output={output_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
