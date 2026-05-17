# Importa il modulo nativo di Python per la generazione di numeri e scelte casuali
import random
# Importa la classe 'Trial' dal file o modulo 'models' per definire la struttura del trial
from models import Trial
# Importa la funzione per calcolare la risposta corretta dal file o modulo 'rules'
from rules import compute_expected_answer

# Definisce la funzione 'generate_trial' che accetta come argomento un generatore di numeri casuali (rng)
# e specifica che restituirà un oggetto di tipo Trial
def generate_trial(rng: random.Random) -> Trial:
    """Genera un nuovo trial casuale bilanciato."""
    
    # Sceglie casualmente la posizione dello stimolo tra "TOP"  e "BOTTOM" usando l'istanza rng
    position = rng.choice(["TOP", "BOTTOM"])
    
    # Definisce una stringa contenente tutte le lettere dell'alfabeto inglese in minuscolo
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    # Seleziona casualmente una singola lettera dalla stringa 'letters' appena definita
    letter = rng.choice(letters)
    
    # Genera un numero intero casuale compreso tra 1 e 9 (inclusi gli estremi)
    number = rng.randint(1, 9)

    # Richiama la funzione esterna per calcolare la risposta corretta in base a posizione, lettera e numero generati
    expected_answer = compute_expected_answer(position, letter, number)

    # Crea e restituisce una nuova istanza della classe Trial, passando tutti i dati raccolti come argomenti
    return Trial(
        position=position,               # Assegna la posizione (TOP o BOTTOM) al campo corrispondente del Trial
        letter=letter,                   # Assegna la lettera estratta al campo corrispondente del Trial
        number=number,                   # Assegna il numero generato al campo corrispondente del Trial
        expected_answer=expected_answer  # Assegna la risposta attesa calcolata al campo corrispondente del Trial
    )
