# Importa il decoratore 'dataclass' dal modulo nativo 'dataclasses'
# Questo decoratore genera automaticamente metodi speciali come __init__ e __repr__
from dataclasses import dataclass

# Applica il decoratore alla classe sottostante per trasformarla in una Data Class
@dataclass
class Trial:
    # Definisce la posizione dello stimolo sullo schermo (es. "TOP" o "BOTTOM") come stringa
    position: str
    
    # Definisce la lettera utilizzata nel trial (es. "a", "b", etc.) come stringa
    letter: str
    
    # Definisce il numero utilizzato nel trial (es. da 1 a 9) come valore intero
    number: int
    
    # Memorizza la risposta corretta attesa dal sistema per questo specifico trial (True o False)
    expected_answer: bool
    
    # Memorizza la risposta data dall'utente. Può essere un booleano (True/False) 
    # oppure None se l'utente non ha ancora risposto. Il valore predefinito è impostato a None.
    user_answer: bool | None = None
    
    # Indica se la risposta dell'utente è corretta. È un booleano con valore predefinito impostato a False.
    is_correct: bool = False
