from rules import is_even, is_vowel, compute_expected_answer

def test_logic():
    assert is_even(2) == True
    assert is_vowel('A') == True
    assert compute_expected_answer("TOP", "A", 2) == True # Alto + Pari
    assert compute_expected_answer("BOTTOM", "A", 2) == True # Basso + Vocale
