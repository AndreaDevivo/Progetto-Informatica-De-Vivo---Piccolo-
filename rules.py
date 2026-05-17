# Definisce la funzione 'is_even' che accetta un numero intero e restituisce un valore booleano
def is_even(number: int) -> bool:
    """Restituisce TRUE se il numero è pari"""          
    return number % 2 == 0     

# Definisce la funzione 'is_vowel' che accetta una stringa (una lettera) e restituisce un valore booleano
def is_vowel(letter: str) -> bool:
    """Restituisce TRUE se la lettera è una vocale"""
    return letter.upper() in 'AEIOU'

# Definisce la funzione principale che calcola la risposta corretta in base a posizione, lettera e numero
def compute_expected_answer(position: str, letter: str, number: int) -> bool:
    """
    Applica la logica di Brain Shift:
    TOP -> Numero Pari?
    BOTTOM -> Vocale? 
    """
    # Se la posizione dello stimolo è in alto ("TOP")
    if position == "TOP":
        # Restituisce il risultato della funzione 'is_even' applicata al numero (True se pari, False se dispari)
        return is_even(number)
    
    # Altrimenti, se la posizione dello stimolo è in basso ("BOTTOM")
    elif position == "BOTTOM":
        # Restituisce il risultato della funzione 'is_vowel' applicata alla lettera (True se vocale, False se consonante)
        return is_vowel(letter)
    
    # Nel caso in cui la posizione non sia né "TOP" né "BOTTOM" (errore di input)
    else:
        # Blocca il programma e lancia un errore di valore specificando il problema
        raise ValueError("Posizione Non valida: Deve essere 'TOP' o 'BOTTOM' ")


