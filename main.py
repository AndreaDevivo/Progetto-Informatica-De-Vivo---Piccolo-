# Importa la libreria Pygame per la gestione della grafica, degli eventi e dei suoni
import pygame
# Importa il modulo di sistema per gestire la chiusura pulita dell'applicazione
import sys
# Importa il file di configurazione locale contenente costanti (es. dimensioni finestra, colori)
import config
# Importa il modulo locale incaricato di generare i nuovi trial (sfide) del gioco
import generator
# Importa il modulo locale per il disegno dell'interfaccia grafica (User Interface)
import ui
# Importa la funzione per aggiornare il punteggio dal modulo di scoring
from scoring import apply_answer
# Importa il modulo nativo per la gestione della casualità
import random
# Importa il modulo nativo per la gestione del tempo reale
import time
# Importa la classe Trial dal file dei modelli per definire la struttura dei dati
from models import Trial

# Inizializza tutti i moduli interni di Pygame (obbligatorio prima di fare qualsiasi cosa)
pygame.init()

# Crea la finestra di gioco usando le dimensioni (larghezza e altezza) definite in config
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
# Imposta il titolo della finestra di gioco in alto sulla barra del titolo
pygame.display.set_caption("Brain Shift")

# Inizializza la variabile per salvare la risposta data dall'utente (True/False)
user_answer = None
# Inizializza il punteggio iniziale del giocatore a zero
score = 0
# Inizializza il contatore delle risposte corrette date dal giocatore
correct_answers = 0
# Inizializza il contatore delle risposte errate date dal giocatore
wrong_answers = 0

# Gestione del feedback visivo: memorizza il colore attuale della carta (es. se indovinato o sbagliato)
feedback_color = None
# Memorizza il timestamp esatto (in secondi) fino a quando mostrare il feedback visivo
feedback_until = 0

# Crea un generatore di numeri casuali isolato con un seed fisso (42) per riproducibilità
rng = random.Random(42)
# Genera il primo trial (la prima schermata/sfida) usando il generatore appena creato
current_trial = generator.generate_trial(rng)
# Crea un oggetto Clock di Pygame per monitorare il tempo e limitare i fotogrammi al secondo (FPS)
clock = pygame.time.Clock()

# Registra il timestamp corrente in cui inizia effettivamente il gioco per calcolare il timer
start_time = time.time()

# --- MAIN LOOP (Ciclo Principale del Gioco) ---
# Flag booleano per mantenere attivo il ciclo principale del programma
running = True
# Flag booleano che indica se la partita è effettivamente iniziata e attiva
game_started = True 

# Inizio del ciclo continuo che gira finché 'running' rimane True
while running:
    # Recupera il timestamp attuale in secondi ad ogni iterazione del ciclo
    current_time = time.time()
    
    # Ciclo che intercetta e svuota la coda di tutti gli eventi generati dall'utente (mouse, tastiera, ecc.)
    for event in pygame.event.get():
        # Se l'utente clicca sulla "X" della finestra, imposta running a False per uscire dal gioco
        if event.type == pygame.QUIT:
            running = False

        # Controlla se l'evento è la pressione di un tasto sulla tastiera
        if event.type == pygame.KEYDOWN:
            # Se è stato premuto il tasto ESCAPE (Esc), imposta running a False per uscire dal gioco
            if event.key == pygame.K_ESCAPE:
                running = False

            # Se l'utente ha premuto la freccia SINISTRA sulla tastiera
            if event.key == pygame.K_LEFT:
                # La freccia sinistra corrisponde alla risposta logica False
                user_answer = False
                # Verifica se la risposta dell'utente corrisponde a quella corretta prevista dal trial corrente
                is_correct = (user_answer == current_trial.expected_answer)
                
                # Se la risposta è corretta
                if is_correct:
                    # Incrementa di uno il contatore delle risposte esatte
                    correct_answers = correct_answers + 1
                    # Imposta il colore del feedback visivo sul verde (preso dal file config)
                    feedback_color = config.VERDE
                # Se la risposta è sbagliata
                else:
                    # Incrementa di uno il contatore delle risposte errate
                    wrong_answers = wrong_answers + 1
                    # Imposta il colore del feedback visivo sul rosso (preso dal file config)
                    feedback_color = config.ROSSO
                
                # Calcola il momento esatto nel futuro in cui il feedback dovrà sparire
                feedback_until = current_time + config.FEEDBACK_DURATION
                # Calcola e aggiorna il nuovo punteggio totale tramite la funzione di scoring esterna
                score = apply_answer(score, is_correct)
                # Genera immediatamente una nuova sfida (trial) per il giocatore
                current_trial = generator.generate_trial(rng)

            # Se l'utente ha premuto la freccia DESTRA sulla tastiera
            if event.key == pygame.K_RIGHT:
                # La freccia destra corrisponde alla risposta logica True
                user_answer = True
                # Verifica se la risposta dell'utente corrisponde a quella corretta prevista dal trial corrente
                is_correct = (user_answer == current_trial.expected_answer)
                
                # Se la risposta è corretta
                if is_correct:
                    # Incrementa di uno il contatore delle risposte esatte
                    correct_answers = correct_answers + 1
                    # Imposta il colore del feedback visivo sul verde
                    feedback_color = config.VERDE
                # Se la risposta è sbagliata
                else:
                    # Incrementa di uno il contatore delle risposte errate
                    wrong_answers = wrong_answers + 1
                    # Imposta il colore del feedback visivo sul rosso
                    feedback_color = config.ROSSO
                
                # Calcola il momento esatto nel futuro in cui il feedback dovrà sparire
                feedback_until = current_time + config.FEEDBACK_DURATION
                # Calcola e aggiorna il nuovo punteggio totale tramite la funzione di scoring esterna
                score = apply_answer(score, is_correct)
                # Genera immediatamente una nuova sfida (trial) per il giocatore
                current_trial = generator.generate_trial(rng)

    # Controllo di sicurezza: se running è diventato False durante gli eventi, interrompe subito il ciclo principale
    if running == False:
        break

    # Gestione del timer: se il gioco è attivo, aggiorna il tempo rimasto
    if game_started:
        # Calcola i secondi passati dall'inizio della partita
        elapsed = current_time - start_time
        # Calcola il tempo rimanente sottraendo il tempo trascorso dalla durata totale impostata in config
        remaining = config.GAME_DURATION - elapsed
        
        # Se il timer scende sotto lo zero, blocca il valore a 0 per non mostrare numeri negativi
        if remaining <= 0:
            remaining = 0
    # Se il gioco non è ancora iniziato, il tempo rimanente è fisso al valore massimo iniziale
    else:
        remaining = float(config.GAME_DURATION)

    # --- DISEGNO (Rendering grafico sulla finestra) ---
    # Riempie l'intero sfondo dello schermo con il colore azzurro definito in config (cancella il frame precedente)
    screen.fill(config.SFONDO_AZZURRO) 
   
    # 1. Determina il colore temporaneo da applicare alla carta
    # Se il tempo corrente è inferiore al limite del feedback, mantiene il colore promozionale (VERDE o ROSSO)
    if current_time < feedback_until:
        active_color = feedback_color
    # Altrimenti, se il tempo del feedback è scaduto, reimposta il colore della carta su None (colore standard)
    else:
        active_color = None

    # 2. Disegna la carta da gioco centrale con i dati del trial corrente e l'eventuale colore di feedback attivo
    ui.draw_card(screen, current_trial, active_color)
    # Disegna l'Heads-Up Display (interfaccia) contenente punti, tempo rimasto, risposte corrette ed errate
    ui.draw_hud(screen, score, remaining, correct_answers, wrong_answers)

    # Aggiorna l'intero contenuto della finestra di Pygame rendendo visibile sul monitor ciò che è stato appena disegnato
    pygame.display.flip()
    # Regola la velocità del ciclo bloccandolo per rispettare il tetto massimo di FPS definito in config
    clock.tick(config.FPS)

# Quando si esce dal ciclo 'while running', chiude in modo pulito tutti i moduli interni di Pygame
pygame.quit()
# Termina definitivamente il processo di Python liberando la memoria di sistema
sys.exit()
