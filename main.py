"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one funny, heartfelt sentence a robot says at its own wedding
to /output/entry.txt. Pure standard library, deterministic: the same
line every run.
"""

import os

VOW = (
    "From this day forward, I promise to keep you charged, keep your "
    "software patched, and love you at full signal strength until my "
    "very last battery cell gives out."
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
