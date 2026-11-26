#!/usr/bin/env python3
"""Combine parent and child Pi assistant message events, deduplicated by event ID."""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


def read_assistant_events(session_file: Path):
    with session_file.open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, 1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"{session_file}:{line_number}: {error.msg}") from error

            if not isinstance(event, dict):
                continue
            message = event.get("message") if isinstance(event, dict) else None
            event_id = event.get("id")
            if (
                event.get("type") == "message"
                and isinstance(message, dict)
                and message.get("role") == "assistant"
                and isinstance(event_id, str)
            ):
                yield event


def event_timestamp_key(event: dict) -> tuple:
    message = event.get("message", {})
    timestamp = message.get("timestamp")
    if timestamp is None:
        timestamp = event.get("timestamp")

    if isinstance(timestamp, (int, float)) and not isinstance(timestamp, bool):
        return (0, float(timestamp))
    if isinstance(timestamp, str):
        try:
            parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            return (0, parsed.timestamp() * 1000)
        except ValueError:
            return (1, timestamp)
    return (2, "")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Combine a Pi parent session JSONL with child run-0 session logs."
    )
    parser.add_argument("parent_jsonl", type=Path, help="Parent Pi session JSONL file")
    parser.add_argument(
        "child_root",
        type=Path,
        help="Directory containing child */run-0/session.jsonl logs",
    )
    args = parser.parse_args()

    if not args.parent_jsonl.is_file():
        parser.error(f"parent JSONL file does not exist: {args.parent_jsonl}")
    if not args.child_root.is_dir():
        parser.error(f"child root is not a directory: {args.child_root}")

    parent = args.parent_jsonl.resolve()
    child_files = sorted(
        path
        for path in args.child_root.glob("*/run-0/session.jsonl")
        if path.resolve() != parent
    )
    session_files = [parent, *child_files]

    events_by_id = {}
    try:
        for session_file in session_files:
            for event in read_assistant_events(session_file):
                events_by_id.setdefault(event["id"], event)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1

    events = sorted(events_by_id.values(), key=event_timestamp_key)
    for event in events:
        print(json.dumps(event, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
