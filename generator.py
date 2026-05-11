import random
from models import Trial
from rules import compute_expected_answer

def generate_trial(rng: random.Random) -> Trial:
    """Genera un nuovo trial casuale bilanciato."""
    position = rng.choice(["TOP", "BOTTOM"])
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter = rng.choice(letters)
    number = rng.randint(1, 9)

    expected_answer = compute_expected_answer(position, letter, number)

    return Trial(
        position=position,
        letter=letter,
        number=number,
        expected_answer=expected_answer
    )
