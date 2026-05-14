from dataclasses import dataclass

@dataclass
class Trial:
    position: str       # "TOP" o "BOTTOM"
    letter: str         # Una lettera (A-Z)
    number: int         # Un numero (1-9)
    expected_answer: bool # Risposta corretta calcolata
