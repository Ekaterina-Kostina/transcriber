from typing import List, Protocol

from core.context import *

class Rule(Protocol):
    def apply(self, phones: List[PhoneToken], ctx: Context) -> List[PhoneToken]:
        ...


class RuleEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def run(self, phones: List[PhoneToken], ctx: Context) -> List[PhoneToken]:
        for r in self.rules:
            phones = r.apply(phones, ctx)
        return phones