import pygame
import sys
import config
import generator
import ui
from scoring import apply_answer
import random
import time
from models import Trial

pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Brain Shift")

user_answer = None
score = 0
correct_answers = 0
wrong_answers = 0

# Gestione del feedback visivo (colore della carta)
feedback_color = None
feedback_until = 0

rng = random.Random(42)
current_trial = generator.generate_trial(rng)
clock = pygame.time.Clock()

# Segno il tempo di inizio per il timer
start_time = time.time()

# --- MAIN LOOP ---
running = True
game_started = True 

while running:
    current_time = time.time()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_LEFT:
                user_answer = False
                is_correct = (user_answer == current_trial.expected_answer)
               
                if is_correct:
                    correct_answers = correct_answers + 1
                    feedback_color = config.VERDE
                else:
                    wrong_answers = wrong_answers + 1
                    feedback_color = config.ROSSO
               
                feedback_until = current_time + config.FEEDBACK_DURATION
                score = apply_answer(score, is_correct)
                current_trial = generator.generate_trial(rng)

            if event.key == pygame.K_RIGHT:
                user_answer = True
                is_correct = (user_answer == current_trial.expected_answer)
               
                if is_correct:
                    correct_answers = correct_answers + 1
                    feedback_color = config.VERDE
                else:
                    wrong_answers = wrong_answers + 1
                    feedback_color = config.ROSSO
               
                feedback_until = current_time + config.FEEDBACK_DURATION
                score = apply_answer(score, is_correct)
                current_trial = generator.generate_trial(rng)

    if running == False:
        break

    if game_started:
        elapsed = current_time - start_time
        remaining = config.GAME_DURATION - elapsed
       
        if remaining <= 0:
            remaining = 0
    else:
        remaining = float(config.GAME_DURATION)

    # --- DISEGNO (Rendering) ---
    screen.fill(config.SFONDO_AZZURRO) 
   
    # 1. Calcolo il colore attivo per la carta (feedback temporaneo)
    if current_time < feedback_until:
        active_color = feedback_color
    else:
        active_color = None

    # 2. Disegno degli elementi tramite il modulo UI aggiornato
    ui.draw_card(screen, current_trial, active_color)
    ui.draw_hud(screen, score, remaining, correct_answers, wrong_answers)

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
sys.exit()
