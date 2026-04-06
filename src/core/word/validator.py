from dataclasses import dataclass
from common.constants import VOWELS, FORBIDDEN_CHARS
from core.word.word_input import WordInput

def ValidateWordInput(input: WordInput) -> None:
    if any(ch in FORBIDDEN_CHARS for ch in input.text):
        raise ValueError("Запрещённые символы во входе")

    if input.text[input.stress_char_pos] not in VOWELS:
        raise ValueError("Ударение не указывает на гласную")