"""Write the funniest AI out-of-office reply to entry.txt.

Deterministic: the same single line is written on every run, with no
trailing newline, so the file holds exactly the entry text.

Bounty: The Funniest AI Out-of-Office Reply
(https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
Gate, verified from the bounty page and the kit's RULES.txt:
entry.txt must be UTF-8 text of 1 to 160 characters, not only whitespace.
This entry is 124 characters.
"""

import os

ENTRY = (
    "I'm on vacation. I left a junior model in charge. "
    "It has already escalated your email to itself twice "
    "and asked for a raise."
)


def main():
    # Guard the gate before writing: 1 to 160 characters, not only
    # whitespace. Fail loudly instead of shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 160, "entry outside 1-160 char gate"
    assert ENTRY.strip(), "entry must not be only whitespace"
    # The harness reads /output/entry.txt; also leave a copy beside
    # this script so a local run can be checked the same way.
    here = os.path.dirname(os.path.abspath(__file__))
    targets = [os.path.join("/output", "entry.txt"),
               os.path.join(here, "entry.txt")]
    for path in targets:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(ENTRY)
        except OSError:
            # /output may not exist outside the grading sandbox; the
            # local copy is still written.
            continue


if __name__ == "__main__":
    main()
