from typing import Set, Dict

VOWELS: Set[str] = set('аеёиоуыэюя')
VOWELS_TRANS: Set[str] = set('aeoiuy')

FORBIDDEN_CHARS: Set[str] = set('ъ')

LETTER_TRANS_MAPPING: Dict[str, str] = {
    # Гласные
    'а': 'a', 'е': 'e', 'ё': 'o', 'и': 'i', 'о': 'o', 
    'у': 'u', 'ы': 'y', 'э': 'e', 'ю': 'u', 'я': 'a',

    # Согласные
    'б': 'b', 'в': 'v',  'г': 'g', 'д': 'd', 'ж': 'zh', 
    'з': 'z', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 
    'н': 'n', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 
    'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh',
    'щ': 'shch'
}

# Сопоставление звуков
VOICELESS_PAIR: Dict[str, str] = {
    "b": "p",
    "d": "t",
    "g": "k",
    "v": "f",
    "z": "s",
    "zh": "sh",
}

# Колонки для анализа
COL_WORD: str = 'Слово'
COL_ORTHOEPIC_TRANS: str = 'Орфоэпическая транскрипция'
COL_STRESSED_WORD: str = 'Слово с ударением'
