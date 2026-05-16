import pygame
from config import *

def draw_card(surface, trial, feedback_color=None):
    """
    Disegna la carta FISSA al centro dello schermo e applica il feedback sul colore.
    """
    # Se c'è un feedback attivo usiamo il colore (VERDE o ROSSO), altrimenti BIANCO
    background_color = feedback_color if feedback_color != None else BIANCO
       
    # Dimensioni della carta da mockup del prof (orizzontale)
    width = 250
    height = 180
    x_pos = WIDTH // 2 - width // 2
    y_pos = HEIGHT // 2 - height // 2 - 20 # Centrata ma leggermente sollevata per fare spazio sotto
       
    # Disegno del rettangolo della carta e del suo bordo nero spesso
    pygame.draw.rect(surface, background_color, (x_pos, y_pos, width, height), border_radius=10)
    pygame.draw.rect(surface, NERO, (x_pos, y_pos, width, height), 4, border_radius=10)
   
    # Disegno del testo dentro la carta (Lettera e Numero)
    card_font = pygame.font.SysFont("Comic Sans MS", 70, bold=True)
    content = f"{trial.letter.upper()}  {trial.number}"
    text_surface = card_font.render(content, True, NERO)
    text_rect = text_surface.get_rect(center=(x_pos + width // 2, y_pos + height // 2))
    surface.blit(text_surface, text_rect)

    # --- CUE VISIVO: DISEGNO DELLA DOMANDA LATERALE ---
    # Scegliamo il testo in base alla posizione logica del trial
    if trial.position == "TOP":
        domanda_testo = "Il numero è pari?"
    else:
        domanda_testo = "La lettera è una vocale?"

    # Dimensioni del box della domanda alla destra della carta
    box_w, box_h = 250, 75
    box_x = x_pos + width + 30
    box_y = y_pos + height // 2 - box_h // 2

    # Disegno il rettangolo bianco della domanda
    pygame.draw.rect(surface, BIANCO, (box_x, box_y, box_w, box_h), border_radius=12)
    pygame.draw.rect(surface, NERO, (box_x, box_y, box_w, box_h), 2, border_radius=12)

    # Scriviamo il testo della domanda dentro il box
    q_font = pygame.font.SysFont("Arial", 22)
    q_surface = q_font.render(domanda_testo, True, NERO)
    q_rect = q_surface.get_rect(center=(box_x + box_w // 2, box_y + box_h // 2))
    surface.blit(q_surface, q_rect)

    # Disegno della freccia nera (un piccolo triangolino/linea che punta alla carta)
    freccia_font = pygame.font.SysFont("Arial", 24, bold=True)
    freccia_surf = freccia_font.render("←", True, NERO)
    freccia_rect = freccia_surf.get_rect(center=(box_x - 12, box_y + box_h // 2))
    surface.blit(freccia_surf, freccia_rect)


def draw_hud(surface, score, time_left, instructions_alpha, correct, wrong):
    """
    Disegna il timer, il punteggio racchiuso nel box e i pulsanti dei contatori in basso.
    """
    hud_font = pygame.font.SysFont("Arial", 28, bold=True)
   
    # 1. Disegno del Timer testuale in alto a sinistra (come da tua richiesta, senza barra)
    time_text = hud_font.render(f"Time: {int(time_left)}s", True, GRIGIO)
    surface.blit(time_text, (20, 20))
   
    # 2. Disegno dello Score in alto a destra dentro il box celeste arrotondato
    score_w, score_h = 130, 40
    score_x = WIDTH - score_w - 20
    score_y = 20
    pygame.draw.rect(surface, CELESTE_PUNTI, (score_x, score_y, score_w, score_h), border_radius=8)
    pygame.draw.rect(surface, NERO, (score_x, score_y, score_w, score_h), 2, border_radius=8)
    
    score_text = hud_font.render(f"Punti: {score}", True, NERO)
    score_rect = score_text.get_rect(center=(score_x + score_w // 2, score_y + score_h // 2))
    surface.blit(score_text, score_rect)
   
    # 3. Disegno delle scritte di Aiuto accademiche (in alto e in basso al centro) con Alpha
    if instructions_alpha > 0:
        help_font = pygame.font.SysFont("Arial", 24, italic=True)
        top_help = help_font.render("TOP: Even Number?", True, GRIGIO)
        bottom_help = help_font.render("BOTTOM: Vowel Letter?", True, GRIGIO)
        
        top_help.set_alpha(instructions_alpha)
        bottom_help.set_alpha(instructions_alpha)
       
        surface.blit(top_help, (WIDTH // 2 - top_help.get_width() // 2, 20))
        surface.blit(bottom_help, (WIDTH // 2 - bottom_help.get_width() // 2, HEIGHT - 40))

    # 4. Disegno dei contatori in basso (Sbagliate e Corrette)
    btn_w, btn_h = 160, 55
    y_btn = HEIGHT - 100
    
    # Pulsante Sbagliate (Rosso)
    x_wrong = WIDTH // 2 - btn_w - 20
    pygame.draw.rect(surface, ROSSO_PULSANTE, (x_wrong, y_btn, btn_w, btn_h), border_radius=12)
    pygame.draw.rect(surface, ROSSO, (x_wrong, y_btn, btn_w, btn_h), 2, border_radius=12)
    wrong_text = hud_font.render(f"Sbagliate: {wrong}", True, TESTO_PULSANTE_ROSSO)
    wrong_rect = wrong_text.get_rect(center=(x_wrong + btn_w // 2, y_btn + btn_h // 2))
    surface.blit(wrong_text, wrong_rect)

    # Pulsante Corrette (Verde)
    x_correct = WIDTH // 2 + 20
    pygame.draw.rect(surface, VERDE_PULSANTE, (x_correct, y_btn, btn_w, btn_h), border_radius=12)
    pygame.draw.rect(surface, VERDE, (x_correct, y_btn, btn_w, btn_h), 2, border_radius=12)
    correct_text = hud_font.render(f"Corrette: {correct}", True, TESTO_PULSANTE_VERDE)
    correct_rect = correct_text.get_rect(center=(x_correct + btn_w // 2, y_btn + btn_h // 2))
    surface.blit(correct_text, correct_rect)


def draw_game_over(surface, final_score):
    """Schermata finale alla scadenza del tempo."""
    surface.fill(NERO)
    title_font = pygame.font.SysFont("Arial", 60, bold=True)
    info_font = pygame.font.SysFont("Arial", 40)
   
    title_surf = title_font.render("GAME OVER", True, ROSSO)
    score_surf = info_font.render(f"Final Score: {final_score}", True, BIANCO)
    retry_surf = info_font.render("Press 'R' to Restart", True, GRIGIO)
   
    surface.blit(title_surf, (WIDTH // 2 - 150, HEIGHT // 2 - 100))
    surface.blit(score_surf, (WIDTH // 2 - 120, HEIGHT // 2))
    surface.blit(retry_surf, (WIDTH // 2 - 160, HEIGHT // 2 + 100))
}
