from typing import Optional, List, Dict, Literal
from dataclasses import dataclass

from core.word.word_input import WordInput
from common.constants import LETTER_TRANS_MAPPING, VOWELS


@dataclass(frozen=True, slots=True)
class FeatureBundle:
    Manner = Literal["vowel", "obstruent", "sonorant"]
    
    voiced: Optional[bool]
    manner: Manner

FEATURES_TABLE: Dict[str, FeatureBundle] = {
    # --- Vowels ---
    "a": FeatureBundle(None, "vowel"),
    "e": FeatureBundle(None, "vowel"),
    "i": FeatureBundle(None, "vowel"),
    "o": FeatureBundle(None, "vowel"),
    "u": FeatureBundle(None, "vowel"),
    "y": FeatureBundle(None, "vowel"),

    # --- Sonorants ---
    "m": FeatureBundle(None, "sonorant"),
    "n": FeatureBundle(None, "sonorant"),
    "l": FeatureBundle(None, "sonorant"),
    "r": FeatureBundle(None, "sonorant"),
    "j": FeatureBundle(None, "sonorant"),

    # --- Voiceless obstruents ---
    "p": FeatureBundle(False, "obstruent"),
    "t": FeatureBundle(False, "obstruent"),
    "k": FeatureBundle(False, "obstruent"),
    "s": FeatureBundle(False, "obstruent"),
    "f": FeatureBundle(False, "obstruent"),


    "sh":   FeatureBundle(False, "obstruent"),
    "h":    FeatureBundle(False, "obstruent"),
    "ts":   FeatureBundle(False, "obstruent"),
    "ch":   FeatureBundle(False, "obstruent"),
    "shch": FeatureBundle(False, "obstruent"),

    # --- Voiced obstruents ---
    "b": FeatureBundle(True, "obstruent"),
    "d": FeatureBundle(True, "obstruent"),
    "g": FeatureBundle(True, "obstruent"),
    "z": FeatureBundle(True, "obstruent"),
    "v": FeatureBundle(True, "obstruent"),
    "zh": FeatureBundle(True, "obstruent"),
}

@dataclass(frozen=True, slots=True)
class GraphemeToken:
    ch: str
    pos: int
    is_vowel: bool
    vowel_idx: Optional[int]
    is_stressed: bool

@dataclass(slots=True)
class PhoneToken:
    sym: str
    is_vowel: bool
    is_stressed: bool
    palatalized: bool
    features: FeatureBundle
    src_pos: int

class Context:
    input: WordInput
    graphemes: List[GraphemeToken]
    phonemes: List[PhoneToken]
    stress_vowel_id: int

def TokenizeWordInput(input: WordInput) -> List[GraphemeToken]:
    tokens: List[GraphemeToken] = []
    for pos, ch in enumerate(input.text):
        is_vowel = ch in VOWELS
        vowel_idx = v_idx if is_vowel else None
        is_stressed = is_vowel and v_idx == input.stress_vowel_idx
        if is_vowel:
            v_idx += 1
        
        tokens.append(GraphemeToken(ch, pos, is_vowel, vowel_idx, is_stressed))

    return tokens


def MapGraphemesToPhonemes(graphemes: List[GraphemeToken]) -> List[PhoneToken]:
    phones = []

    for g in graphemes:
        if g.ch == "ь":
            phones[-1].palatalized = True
            continue

        sym = LETTER_TRANS_MAPPING[g.ch]
        phones.append(
            PhoneToken(
                sym=sym,
                is_vowel=g.is_vowel,
                is_stressed=g.is_stressed,
                palatalized=False,
                features=FEATURES_TABLE[sym],
                src_pos=g.pos,
            )
        )

    return phones