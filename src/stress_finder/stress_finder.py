from common.constants import VOWELS, VOWELS_TRANS

"""
Определяет, которая по счёту гласная является ударной
в транскрипции словаря.

Логика: ударная гласная помечена цифрой 0 (u0, a0, o0...).
Считаем только гласные токены (вида буква+цифра),
возвращаем порядковый номер ударной.

Пример:
    '* a1 p s a1 l' u0 t + n + a4'
    гласные по порядку: a1(1), a1(2), u0(3*), a4(4)
    → возвращает 3
"""

def find_stress_vowel_in_transcription(transcription: str) -> int | None:
    tokens: list[str] = transcription.lower().split(' ')

    vowel_count: int = 0
    for token in tokens:
        if(len(token) > 1 and token[0] in VOWELS_TRANS and token[-1].isdigit()):
            vowel_count += 1
            if token[-1] == '0':
                return vowel_count

    return None

def insert_stress(word: str, stress_vowel_pos: int) -> str:
    vowels_count: int = 0
    res: list = []
    for letter in word.lower():
        res.append(letter)
        if(letter in VOWELS):
            vowels_count += 1
            if(vowels_count == stress_vowel_pos):
                res.append('0')

    return ''.join(res)

def restore_stress_by_transcription(raw_word: str, transcription: str) -> str | None:
    stress_pos: int = find_stress_vowel_in_transcription(transcription)

    if(stress_pos is None):
        return None

    return insert_stress(raw_word, stress_pos)
