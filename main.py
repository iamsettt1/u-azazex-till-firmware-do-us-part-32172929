"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one funny, heartfelt sentence a robot says at its own wedding
to /output/entry.txt. Pure standard library, deterministic: the same
line every run. The vow promises to reboot beside the partner each
morning, sync calendars, and keep loving in every version of itself —
past the warranty and beyond.
"""

import os

VOW = (
    "I promise to reboot beside you every morning, sync my calendar "
    "to yours, and love you in every version of me until my warranty "
    "runs out — and long after."
)


def main() -> None:
    # Gate check: the entry must be UTF-8 text of 1 to 200 characters,
    # not only white space, and exactly one sentence.
    assert 1 <= len(VOW) <= 200, "vow must fit the 200-character gate"
    assert VOW.strip() == VOW and VOW.count(".") == 1, "vow must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
