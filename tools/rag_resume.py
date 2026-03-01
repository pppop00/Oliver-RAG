#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rag_lib.experience_sync import sync_experience
from rag_lib.resume_generator import generate_role_resume


def cmd_add_experience(args: argparse.Namespace) -> int:
    root = Path(__file__).resolve().parents[1]
    payload_path = Path(args.payload).resolve()
    result = sync_experience(root=root, payload_path=payload_path)

    print(f"experience_file={result.experience_file}")
    for p in result.updated_files:
        print(f"updated={p}")

    print(f"gate_passed={str(result.gate_passed).lower()}")
    if not result.gate_passed:
        for gate_name, items in result.gate_details.items():
            if items:
                print(f"{gate_name} issues:")
                for item in items:
                    print(f"  - {item}")
        return 2
    return 0


def cmd_generate_role_resume(args: argparse.Namespace) -> int:
    root = Path(__file__).resolve().parents[1]
    result = generate_role_resume(root=root, role=args.role)

    print(f"output={result.output_path}")
    print(f"profile_fallback={str(result.profile_fallback).lower()}")
    for name, ok, detail in result.preflight.checks:
        print(f"preflight.{name}={str(ok).lower()} detail={detail}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Personal RAG resume automation")
    sub = parser.add_subparsers(dest="command", required=True)

    add_exp = sub.add_parser("add-experience", help="Sync one new experience into RAG sources")
    add_exp.add_argument("--payload", required=True, help="Path to JSON payload")
    add_exp.set_defaults(func=cmd_add_experience)

    gen = sub.add_parser("generate-role-resume", help="Generate role-tailored one-page DOCX")
    gen.add_argument("--role", required=True, help="Target role name")
    gen.set_defaults(func=cmd_generate_role_resume)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
