import json
from pathlib import Path


def load_texts() -> dict[str, dict[str, str]]:
    path = Path.cwd() / 'src' / 'components' / 'texts' / 'cars.json'
    with open(path) as f:
        data = json.load(f)
    return data


TEXTS: dict[str, dict[str, str]] = load_texts()
CATEGORIES: list[str] = [key for key in TEXTS.keys()]
TITLES: list[str] = [TEXTS[cat]['título'] for cat in CATEGORIES]
ANSWERS: list[str] = ['1', '2', '3', '4']
SCORES: list[str] = ['1', '1.5', '2', '2.5', '3', '3.5', '4']
