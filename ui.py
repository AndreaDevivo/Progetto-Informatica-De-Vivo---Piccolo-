# Importa la libreria Pygame per le funzionalità di disegno e gestione dei font
import pygame
# Importa tutte le costanti (colori, dimensioni, ecc.) definite nel file config.py
from config import *

# Definisce la funzione per disegnare la carta da gioco centrale e la sua domanda associata
def draw_card(surface, trial, feedback_color=None):
    """
    Disegna la carta FISSA al centro dello schermo e applica il feedback sul colore.
    """
    # Se è presente un colore di feedback (risposta data), lo usa, altrimenti imposta il colore di sfondo standard (BIANCO)
    background_color = feedback_color if feedback_color != None else BIANCO
        
    # Definisce la larghezza in pixel della carta centrale
    width = 250
    # Definisce l'altezza in pixel della carta centrale
    height = 180
    # Calcola la coordinata X per centrare la carta orizzontalmente rispetto alla larghezza dello schermo (WIDTH)
    x_pos = WIDTH // 2 - width // 2
    # Calcola la coordinata Y per centrare la carta verticalmente, sollevandola di 20 pixel per lasciare spazio sotto
    y_pos = HEIGHT // 2 - height // 2 - 20 
        
    # Disegna il rettangolo pieno dello sfondo della carta (bianco, verde o rosso) con angoli arrotondati (raggio 10)
    pygame.draw.rect(surface, background_color, (x_pos, y_pos, width, height), border_radius=10)
    # Disegna solo il contorno (spessore 4 pixel) nero della carta, mantenendo gli angoli arrotondati
    pygame.draw.rect(surface, NERO, (x_pos, y_pos, width, height), 4, border_radius=10)
    
    # Inizializza il font Comic Sans MS a dimensione 70 in grassetto per il contenuto della carta
    card_font = pygame.font.SysFont("Comic Sans MS", 70, bold=True)
    # Crea la stringa di testo combinando la lettera (convertita in maiuscolo) e il numero, separati da spazi
    content = f"{trial.letter.upper()}  {trial.number}"
    # Trasforma la stringa di testo in una superficie grafica renderizzata di colore nero
    text_surface = card_font.render(content, True, NERO)
    # Crea il rettangolo di posizionamento del testo, centrandolo esattamente nel mezzo della carta
    text_rect = text_surface.get_rect(center=(x_pos + width // 2, y_pos + height // 2))
    # Copia la superficie del testo sullo schermo (surface) nella posizione calcolata dal rettangolo
    surface.blit(text_surface, text_rect)

    # ---  DISEGNO DELLA DOMANDA LATERALE ---
    # Controlla la posizione logica del trial corrente per determinare quale testo mostrare
    if trial.position == "TOP":
        # Se la posizione è TOP, la domanda riguarda la parità del numero
        domanda_testo = "Il numero è pari?"
    else:
        # Altrimenti (se è BOTTOM), la domanda riguarda la presenza di una vocale
        domanda_testo = "La lettera è una vocale?"

    # Definisce la larghezza (250px) e l'altezza (75px) del box che conterrà il testo della domanda
    box_w, box_h = 250, 75
    # Calcola la coordinata X del box posizionandolo a destra della carta, distanziato di 30 pixel
    box_x = x_pos + width + 30
    # Calcola la coordinata Y per allineare verticalmente il centro del box con il centro della carta
    box_y = y_pos + height // 2 - box_h // 2

    # Disegna il rettangolo di sfondo bianco per il box della domanda con angoli arrotondati (raggio 12)
    pygame.draw.rect(surface, BIANCO, (box_x, box_y, box_w, box_h), border_radius=12)
    # Disegna il contorno nero (spessore 2 pixel) attorno al box della domanda
    pygame.draw.rect(surface, NERO, (box_x, box_y, box_w, box_h), 2, border_radius=12)

    # Inizializza il font Arial a dimensione 22 per il testo della domanda
    q_font = pygame.font.SysFont("Arial", 22)
    # Trasforma il testo della domanda in una superficie grafica renderizzata di colore nero
    q_surface = q_font.render(domanda_testo, True, NERO)
    # Calcola il rettangolo di posizionamento per centrare il testo perfettamente all'interno del suo box
    q_rect = q_surface.get_rect(center=(box_x + box_w // 2, box_y + box_h // 2))
    # Copia il testo della domanda sullo schermo nella posizione definita dal suo rettangolo
    surface.blit(q_surface, q_rect)

    # Inizializza un font Arial a dimensione 24 in grassetto per disegnare la freccia indicatrice
    freccia_font = pygame.font.SysFont("Arial", 24, bold=True)
    # Renderizza il carattere speciale freccia a sinistra "←" in colore nero
    freccia_surf = freccia_font.render("←", True, NERO)
    # Posiziona la freccia a sinistra del box della domanda (rientrata di 12 pixel) e allineata al centro verticale
    freccia_rect = freccia_surf.get_rect(center=(box_x - 12, box_y + box_h // 2))
    # Copia il simbolo della freccia sullo schermo
    surface.blit(freccia_surf, freccia_rect)


# Definisce la funzione per disegnare gli elementi della HUD (Heads-Up Display) come timer e punteggi
def draw_hud(surface, score, time_left, correct, wrong):
    """
    Disegna il timer, il punteggio racchiuso nel box e i pulsanti dei contatori in basso.
    """
    # Inizializza un font Arial a dimensione 28 in grassetto per tutte le scritte della HUD
    hud_font = pygame.font.SysFont("Arial", 28, bold=True)
    
    # 1. Disegno del Timer testuale in alto a sinistra
    # Renderizza la stringa con il tempo rimasto convertito in intero (es. "Time: 45s") in colore grigio
    time_text = hud_font.render(f"Time: {int(time_left)}s", True, GRIGIO)
    # Disegna il testo del timer alle coordinate fisse (x=20, y=20) sullo schermo
    surface.blit(time_text, (20, 20))
    
    # 2. Disegno dello Score in alto a destra dentro il box celeste arrotondato
    # Definisce larghezza (130px) e altezza (40px) per il box del punteggio
    score_w, score_h = 130, 40
    # Calcola la coordinata X posizionando il box sul lato destro dello schermo meno la larghezza e un margine di 20px
    score_x = WIDTH - score_w - 20
    # Imposta la coordinata Y a 20 pixel dal bordo superiore dello schermo
    score_y = 20
    # Disegna lo sfondo del box usando il colore azzurro specifico per i punti con angoli arrotondati
    pygame.draw.rect(surface, CELESTE_PUNTI, (score_x, score_y, score_w, score_h), border_radius=8)
    # Disegna il contorno nero di spessore 2 pixel attorno al box del punteggio
    pygame.draw.rect(surface, NERO, (score_x, score_y, score_w, score_h), 2, border_radius=8)
    
    # Renderizza il testo del punteggio corrente (es. "Punti: 5") in colore nero
    score_text = hud_font.render(f"Punti: {score}", True, NERO)
    # Centra perfettamente il testo del punteggio all'interno del perimetro del suo box celeste
    score_rect = score_text.get_rect(center=(score_x + score_w // 2, score_y + score_h // 2))
    # Copia il testo del punteggio renderizzato sullo schermo
    surface.blit(score_text, score_rect)

    # 3. Disegno dei contatori in basso (Sbagliate e Corrette)
    # Definisce la dimensione standard per i due box/pulsanti dei contatori in basso
    btn_w, btn_h = 160, 55
    # Imposta la coordinata Y per entrambi i pulsanti, posizionandoli a 100 pixel dal fondo dello schermo
    y_btn = HEIGHT - 100
    
    # Pulsante Sbagliate (Rosso)
    # Calcola la coordinata X per posizionare il pulsante rosso a sinistra rispetto al centro dello schermo
    x_wrong = WIDTH // 2 - btn_w - 20
    # Disegna la forma rettangolare del pulsante con il colore rosso di sfondo (sfumatura pulsante)
    pygame.draw.rect(surface, ROSSO_PULSANTE, (x_wrong, y_btn, btn_w, btn_h), border_radius=12)
    # Disegna la linea di contorno del pulsante usando il colore rosso acceso primario
    pygame.draw.rect(surface, ROSSO, (x_wrong, y_btn, btn_w, btn_h), 2, border_radius=12)
    # Renderizza la scritta interna con il contatore degli errori (es. "Sbagliate: 2") col rispettivo colore del testo
    wrong_text = hud_font.render(f"Sbagliate: {wrong}", True, TESTO_PULSANTE_ROSSO)
    # Allinea e centra il testo degli errori all'interno dell'area del suo pulsante rosso
    wrong_rect = wrong_text.get_rect(center=(x_wrong + btn_w // 2, y_btn + btn_h // 2))
    # Copia il testo degli errori sullo schermo
    surface.blit(wrong_text, wrong_rect)

    # Pulsante Corrette (Verde)
    # Calcola la coordinata X per posizionare il pulsante verde a destra rispetto al centro dello schermo (lasciando spazio)
    x_correct = WIDTH // 2 + 20
    # Disegna la forma rettangolare dello sfondo del pulsante con la tinta verde per i pulsanti
    pygame.draw.rect(surface, VERDE_PULSANTE, (x_correct, y_btn, btn_w, btn_h), border_radius=12)
    # Disegna la linea di bordo del pulsante usando il colore verde acceso primario
    pygame.draw.rect(surface, VERDE, (x_correct, y_btn, btn_w, btn_h), 2, border_radius=12)
    # Renderizza il testo con il contatore delle risposte esatte (es. "Corrette: 12") col rispettivo colore del testo
    correct_text = hud_font.render(f"Corrette: {correct}", True, TESTO_PULSANTE_VERDE)
    # Allinea e centra il testo delle risposte esatte all'interno dell'area del suo pulsante verde
    correct_rect = correct_text.get_rect(center=(x_correct + btn_w // 2, y_btn + btn_h // 2))
    # Copia il testo delle risposte esatte sullo schermo
    surface.blit(correct_text, correct_rect)


# Definisce la funzione per mostrare la schermata finale di interruzione del gioco
def draw_game_over(surface, final_score):
    """Schermata finale alla scadenza del tempo."""
    # Cancella tutto lo schermo riempiendolo completamente di colore NERO
    surface.fill(NERO)
    # Configura un font Arial grande (60px) in grassetto dedicato al titolo principale
    title_font = pygame.font.SysFont("Arial", 60, bold=True)
    # Configura un secondo font Arial di medie dimensioni (40px) per i testi informativi secondari
    info_font = pygame.font.SysFont("Arial", 40)
   
    # Genera la grafica per la scritta di fine gioco "GAME OVER" colorata in ROSSO
    title_surf = title_font.render("GAME OVER", True, ROSSO)
    # Genera la stringa grafica con il punteggio finale raggiunto dal giocatore (es. "Final Score: 15") in BIANCO
    score_surf = info_font.render(f"Final Score: {final_score}", True, BIANCO)
    # Genera la stringa di istruzioni per informare l'utente come rigiocare ("Press 'R' to Restart") in GRIGIO
    retry_surf = info_font.render("Press 'R' to Restart", True, GRIGIO)
   
    # Disegna il titolo "GAME OVER" posizionandolo vicino al centro ma spostato leggermente in alto (-100px)
    surface.blit(title_surf, (WIDTH // 2 - 150, HEIGHT // 2 - 100))
    # Disegna l'indicazione del punteggio finale esattamente sulla linea centrale dello schermo
    surface.blit(score_surf, (WIDTH // 2 - 120, HEIGHT // 2))
    # Disegna l'istruzione di riavvio spostata più in basso (+100px) rispetto al centro dello schermo
    surface.blit(retry_surf, (WIDTH // 2 - 160, HEIGHT // 2 + 100))
