#!/usr/bin/env python3
"""Validate a 3-12 second nine-grid storyboard markdown file."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SHOT_RE = re.compile(r"^###\s+(SHOT-\d{2})\b", re.MULTILINE)
REQUIRED_FIELDS = (
    "来源/覆盖：",
    "职责：",
    "目的：",
    "时间范围：",
    "起点：",
    "动作：",
    "终点：",
    "摄影机：",
    "情绪/信息变化：",
    "风险：",
    "参考用途：",
    "声音/台词：",
)
TIME_RE = re.compile(
    r"时间范围：\s*(\d+(?:\.\d+)?)\s*(?:s|秒)?\s*[-–—]\s*(\d+(?:\.\d+)?)\s*(?:s|秒)?",
    re.IGNORECASE,
)
BANNED_PHRASES = (
    "camera pans across the grid",
    "camera pans across the storyboard",
    "镜头扫过九宫格",
    "镜头扫过漫画页",
    "comic book page comes alive",
)


def parse_time(block: str) -> tuple[float, float] | None:
    match = TIME_RE.search(block)
    if not match:
        return None
    return float(match.group(1)), float(match.group(2))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path, help="Storyboard markdown file")
    parser.add_argument("--min-shots", type=int, default=9)
    parser.add_argument("--max-shots", type=int, default=9)
    parser.add_argument("--min-duration", type=float, default=3.0)
    parser.add_argument("--max-duration", type=float, default=12.0)
    args = parser.parse_args()

    text = args.markdown.read_text(encoding="utf-8")
    errors: list[str] = []
    shots = SHOT_RE.findall(text)

    if not (args.min_shots <= len(shots) <= args.max_shots):
        errors.append(
            f"Expected {args.min_shots}-{args.max_shots} shots, found {len(shots)}."
        )

    expected_ids = [f"SHOT-{index:02d}" for index in range(1, len(shots) + 1)]
    if shots != expected_ids:
        errors.append(f"Shot IDs are missing, duplicated, or out of order: {shots}")

    blocks = re.split(r"^###\s+SHOT-\d{2}\b", text, flags=re.MULTILINE)[1:]
    times: list[tuple[float, float]] = []

    for index, block in enumerate(blocks, 1):
        missing = [field for field in REQUIRED_FIELDS if field not in block]
        if missing:
            errors.append(f"SHOT-{index:02d} is missing fields: {', '.join(missing)}")

        time = parse_time(block)
        if time is None:
            errors.append(f"SHOT-{index:02d} has no parseable continuous time range.")
            continue
        if time[1] <= time[0]:
            errors.append(
                f"SHOT-{index:02d} end time must be greater than start time: {time[0]}-{time[1]}s."
            )
        times.append(time)

    if times:
        if abs(times[0][0]) > 0.0001:
            errors.append(f"First shot must start at 0.0s, found {times[0][0]}s.")
        for index in range(1, len(times)):
            previous_end = times[index - 1][1]
            current_start = times[index][0]
            if abs(previous_end - current_start) > 0.0001:
                errors.append(
                    f"SHOT-{index + 1:02d} starts at {current_start}s, "
                    f"but SHOT-{index:02d} ends at {previous_end}s."
                )
        total_duration = times[-1][1]
        if not (args.min_duration <= total_duration <= args.max_duration):
            errors.append(
                f"Total duration must be {args.min_duration}-{args.max_duration}s, "
                f"found {total_duration}s."
            )
    else:
        total_duration = 0.0

    lowered = text.lower()
    for banned in BANNED_PHRASES:
        if banned in lowered:
            errors.append(f"Banned storyboard-as-object instruction found: {banned}")

    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"VALID: {len(shots)} shots, {total_duration:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
