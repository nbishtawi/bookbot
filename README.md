# BookBot

Small Python tool that analyzes a plain-text book and prints a short report:
- total word count
- per-character frequency (a–z), case-insensitive
- sorted output for quick scanning

---

## Features

- Counts letters a–z (case-insensitive, ignores punctuation/numbers)
- Reports total words
- Sorted frequency table (highest → lowest)
- No external dependencies (pure standard library)

---

## Quickstart

**Requirements:** Python 3.10+ (any recent 3.x should work)

```bash
# 1) Clone
git clone https://github.com/nbishtawi/bookbot
cd bookbot

# 2) Put a text file in a local "books/" folder (example below)
mkdir -p books
curl -L -o books/frankenstein.txt https://www.gutenberg.org/cache/epub/84/pg84.txt

# 3) Run
python main.py <path_to_book>
