import pygame
import random

# Inicjalizacja biblioteki Pygame
pygame.init()

# Ustawienia ekranu
szerokosc = 800
wysokosc = 600
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Gra Snake")

# Kolory
bialy = (255, 255, 255)
czarny = (0, 0, 0)
zielony = (0, 255, 0)
czerwony = (255, 0, 0)

# Rozmiar bloku
rozmiar_bloku = 20

# Prędkość węża
predkosc = 10

# Funkcja generująca jedzenie dla węża
def generuj_jedzenie():
    x = random.randrange(0, szerokosc - rozmiar_bloku, rozmiar_bloku)
    y = random.randrange(0, wysokosc - rozmiar_bloku, rozmiar_bloku)
    return pygame.Rect(x, y, rozmiar_bloku, rozmiar_bloku)

# Inicjalizacja pozycji węża i jedzenia
waz = [pygame.Rect(0, 0, rozmiar_bloku, rozmiar_bloku)]
jedzenie = generuj_jedzenie()

# Kierunek węża (0 - w prawo, 1 - w dół, 2 - w lewo, 3 - w górę)
kierunek = 0

# Główna pętla gry
gra_aktywna = True
clock = pygame.time.Clock()
while gra_aktywna:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gra_aktywna = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and kierunek != 2:
                kierunek = 0
            elif event.key == pygame.K_DOWN and kierunek != 3:
                kierunek = 1
            elif event.key == pygame.K_LEFT and kierunek != 0:
                kierunek = 2
            elif event.key == pygame.K_UP and kierunek != 1:
                kierunek = 3

    # Poruszanie wężem
    if kierunek == 0:
        waz.insert(0, pygame.Rect(waz[0].x + rozmiar_bloku, waz[0].y, rozmiar_bloku, rozmiar_bloku))
    elif kierunek == 1:
        waz.insert(0, pygame.Rect(waz[0].x, waz[0].y + rozmiar_bloku, rozmiar_bloku, rozmiar_bloku))
    elif kierunek == 2:
        waz.insert(0, pygame.Rect(waz[0].x - rozmiar_bloku, waz[0].y, rozmiar_bloku, rozmiar_bloku))
    elif kierunek == 3:
        waz.insert(0, pygame.Rect(waz[0].x, waz[0].y - rozmiar_bloku, rozmiar_bloku, rozmiar_bloku))

    # Sprawdzenie kolizji z jedzeniem
    if waz[0].colliderect(jedzenie):
        jedzenie = generuj_jedzenie()
    else:
        waz.pop()

    # Sprawdzenie kolizji z krawędziami ekranu
    if waz[0].x < 0 or waz[0].x >= szerokosc or waz[0].y < 0 or waz[0].y >= wysokosc:
        gra_aktywna = False

    # Sprawdzenie kolizji z samym sobą
    if waz[0] in waz[1:]:
        gra_aktywna = False

    # Aktualizacja ekranu
    ekran.fill(czarny)
    pygame.draw.rect(ekran, zielony, jedzenie)
    for segment in waz:
        pygame.draw.rect(ekran, czerwony, segment)

    pygame.display.flip()
    clock.tick(predkosc)

# Zakończenie gry
pygame.quit()
