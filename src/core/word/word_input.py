from dataclasses import dataclass
from common.constants import VOWELS

@dataclass(frozen=True, slots=True)
class WordInput:
    raw: str
    text: str
    stress_vowel_idx: int
    stress_char_pos: int

    @classmethod
    def from_marked(cls, raw: str) -> "WordInput":
        if not isinstance(raw, str):
            raise TypeError("Ожидается строка.")

        raw = raw.strip()
        if not raw:
            raise ValueError("Пустой ввод.")

        if raw.count("0") != 1:
            raise ValueError("Ожидается ровно один символ '0'.")

        zero_pos = raw.index("0")
        if zero_pos == 0:
            raise ValueError("'0' не может быть первым символом.")

        stressed_char = raw[zero_pos - 1].lower()
        if stressed_char not in VOWELS:
            raise ValueError("'0' должен идти сразу после гласной.")

        text = (raw[:zero_pos] + raw[zero_pos + 1:]).lower()
        stress_char_pos = zero_pos - 1
        stress_vowel_idx = sum(
            1 for ch in text[:stress_char_pos] if ch in VOWELS
        )

        return cls(
            raw=raw,
            text=text,
            stress_vowel_idx=stress_vowel_idx,
            stress_char_pos=stress_char_pos,
        )