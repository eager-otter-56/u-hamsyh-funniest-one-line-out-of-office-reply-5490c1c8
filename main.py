"""Entry for make.fun: Funniest One-Line Out-of-Office Reply.

Writes a single-line out-of-office auto-reply to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output). Gate: UTF-8, 1-160 chars,
not only whitespace, one line.
"""

import os

ENTRY = "I'm away until Thursday. My out-of-office approved itself 47 times overnight \u2014 please direct all complaints to it."
# The joke: the auto-reply is the agent's own approval loop turned on
# itself — it approved itself, so complaints go to it, not to me.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 160, f"entry length {len(text)} outside 1-160"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
