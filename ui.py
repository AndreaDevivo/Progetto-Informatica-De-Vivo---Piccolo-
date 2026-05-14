import pygame
from config import *

def draw_card(surface, trial, feedback_color=None):
    """
    Disegna la carta e gestisce il colore e la posizione.
    """
   
    # --- FEEDBACK COLOR LOGIC ---
    # Se feedback_color non è None, usiamo il colore ricevuto (VERDE o ROSSO)
    if feedback_color != None:
        background_color = feedback_color
    else:
        # Altrimenti usiamo il colore standard della carta
        background_color = BIANCO
       
    width = 200
    height = 250
    x_pos = WIDTH // 2 - width // 2
   
    # --- POSITION LOGIC ---
    # Se la posizione è "TOP", la carta va in alto
    if trial.position == "TOP":
        y_pos = 50
    else:
        # Altrimenti la carta va in basso
        y_pos = HEIGHT - 300
       
    # Disegno del rettangolo della carta
    pygame.draw.rect(surface, background_color, (x_pos, y_pos, width, height))
    # Disegno del bordo nero
    pygame.draw.rect(surface, NERO, (x_pos, y_pos, width, height), 3)
   
    # --- TEXT LOGIC ---
    card_font = pygame.font.SysFont("Arial", 80, bold=True)
    # Prepariamo la stringa (Esempio: "A 5")
    content = f"{trial.letter.upper()} {trial.number}"
    text_surface = card_font.render(content, True, NERO)
   
    # Centriamo il testo all'interno del rettangolo della carta
    text_rect = text_surface.get_rect(center=(x_pos + width // 2, y_pos + height // 2))
    surface.blit(text_surface, text_rect)


def draw_hud(surface, score, time_left, instructions_alpha):
    """
    Disegna il punteggio, il tempo e le istruzioni con trasparenza.
    """
   
    hud_font = pygame.font.SysFont("Arial", 30)
   
    # Disegno dello Score (Punti)
    score_text = hud_font.render(f"Score: {score}", True, VERDE)
    surface.blit(score_text, (WIDTH - 150, 20))
   
    # Disegno del Timer
    time_text = hud_font.render(f"Time: {int(time_left)}s", True, BIANCO)
    surface.blit(time_text, (20, 20))
   
    # --- INSTRUCTIONS FADING LOGIC ---
    # Se instructions_alpha è maggiore di zero, disegniamo gli aiuti
    if instructions_alpha > 0:
        help_font = pygame.font.SysFont("Arial", 20, italic=True)
        top_help = help_font.render("TOP: Even Number?", True, GRIGIO)
        bottom_help = help_font.render("BOTTOM: Vowel Letter?", True, GRIGIO)
       
        # Applichiamo il livello di trasparenza (Alpha)
        top_help.set_alpha(instructions_alpha)
        bottom_help.set_alpha(instructions_alpha)
       
        # Posizionamento degli aiuti
        surface.blit(top_help, (WIDTH // 2 - 80, 20))
        surface.blit(bottom_help, (WIDTH // 2 - 80, HEIGHT - 40))


def draw_game_over(surface, final_score):
    """
    Disegna la schermata finale quando il tempo scade.
    """
    surface.fill(NERO)
    title_font = pygame.font.SysFont("Arial", 60, bold=True)
    info_font = pygame.font.SysFont("Arial", 40)
   
    title_surf = title_font.render("GAME OVER", True, ROSSO)
    score_surf = info_font.render(f"Final Score: {final_score}", True, BIANCO)
    retry_surf = info_font.render("Press 'R' to Restart", True, GRIGIO)
   
    # Centriamo i testi sullo schermo
    surface.blit(title_surf, (WIDTH // 2 - 150, HEIGHT // 2 - 100))
    surface.blit(score_surf, (WIDTH // 2 - 120, HEIGHT // 2))
    surface.blit(retry_surf, (WIDTH // 2 - 160, HEIGHT // 2 + 100))
