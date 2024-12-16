"""
Created on 12/15/2024
by Jye-Ming Serres
"""
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
TARGET_FRAME_RATE = 100

def blit_fps(str, destination):
    fps_font = pygame.font.SysFont('comicsans', 16)
    fps_surface = fps_font.render(str, True, (200, 200, 200))
    destination.blit(fps_surface, (5, 0))
