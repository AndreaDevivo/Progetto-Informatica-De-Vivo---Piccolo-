import pytest

try:
    from scoring import apply_answer
except ImportError:
    apply_answer = None

def test_structure_check():
    assert apply_answer is not None, "Non trovo 'apply_answer' in 'scoring.py'."

def test_correct_answer_increases_score_by_10():
    assert apply_answer(0, True) == 10
    assert apply_answer(50, True) == 60

def test_wrong_answer_does_not_increase_score():
    assert apply_answer(100, False) <= 100
    assert apply_answer(0, False) <= 0

def test_wrong_answer_consistent_policy():
    delta_1 = 50 - apply_answer(50, False)
    delta_2 = 200 - apply_answer(200, False)
    assert delta_1 == delta_2, "La policy per la risposta errata non è coerente."

def test_correct_answer_from_negative_score():
    assert apply_answer(-5, True) == 5

def test_apply_answer_is_pure():
    assert apply_answer(100, True) == apply_answer(100, True)

def test_sequence_of_answers():
    score = 0
    for _ in range(5):
        score = apply_answer(score, True)
    assert score == 50

def test_return_type_is_int():
    result = apply_answer(10, True)
    assert isinstance(result, int)
