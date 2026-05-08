def is_even(number:int) -> bool:
    """Restituisce TRUE se il numero è pari"""          
    return number % 2 == 0     

def is_vowel(letter:str) -> bool:
    """Restituisce TRUE se la lettera è una vocale"""
    return letter.upper() in 'AEIOU'

def compute_expected_answer(position:str, letter:str , number:int) -> bool:
    """
    Applica la logica di Brain Shift:
    TOP -> Numero Pari?
    BOTTOM -> Vocale? 

    """
    if position == "TOP":
        return is_even(number)
    elif position == "BOTTOM":
        return is_vowel(letter)
    else:
        raise ValueError("Posizione Non valida: Deve essere 'TOP' o 'BOTTOM' ")


