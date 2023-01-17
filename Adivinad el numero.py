import pygame, sys, random
pygame.init()
from pygame import mixer
puntuacion=0
# /* Clases */
class text(object):
    def __init__(self, text, color, position = None):
        self.font = pygame.font.Font("arial.ttf", 32)
        self.text = self.font.render(text,True, color)
        self.object = self.text.get_rect()
        self.color = color
        self.currentText = text
        if position:
            self.position = position
            self.object.center = position

    def draw(self, surface):
        surface.blit(self.text, self.object)

    def change(self, text):
        self.text = self.font.render(text, True, self.color)
        self.object = self.text.get_rect()
        self.currentText = text
        try:
            self.object.center = self.position
        except:
            print("Sin posicion")

    def add(self, text):
        self.text = self.font.render(self.currentText + text, True, self.color)
        self.object = self.text.get_rect()
        self.currentText += text
        try:
            self.object.center = self.position
        except:
            print("Sin posicion")

    def subtract(self):
        try:
            lis = list(self.currentText)
            lis.pop()
            self.currentText = ''.join(lis)
            self.text = self.font.render(self.currentText, True, self.color)
            self.object = self.text.get_rect()
            try:
                self.object.center = self.position
            except:
                print("Sin posicion")
        except:
            print("eliminar de la lista")

# Colors
BLACK = (30,30,30)
ivory1 = (255,255,240)
green = (00,80,00)

# /* Variables */
WIDTH,HEIGHT = 1280,720
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Adivínad el número!")
TEXT = text("", ivory1, ((WIDTH/2), HEIGHT/2 + 55))
TEXT2 = text("Adivínad el número!", green, (WIDTH/2,HEIGHT/2))
RANDOM_NUMBER = random.randint(0,100)
clock = pygame.time.Clock()
# /* Functions */
def up(event):
    if event.unicode == "\x08":
        TEXT.subtract()
    elif event.unicode == "\r":
            global RANDOM_NUMBER
            if str(TEXT.currentText) == str(RANDOM_NUMBER):
                global puntuacion
                puntuacion+=1
                TEXT2.change(f"{TEXT.currentText} Has adividado! tienes: %i ptos" %(puntuacion))
                mixer.init()
                mixer.music.load('victoria.mp3')
                mixer.music.play()
                RANDOM_NUMBER = random.randint(0,100)
            elif not TEXT.currentText.isdigit():
                TEXT2.change(f"{TEXT.currentText} esto no es un número! ",)
            elif int(TEXT.currentText) > 100:
                TEXT2.change(f"{TEXT.currentText} Es solo de 0 a 100! ",)
            else:
                TEXT2.change(f"{TEXT.currentText} No has adivinado! ")
    else:
        TEXT.add(event.unicode)
        

def draw():
    pygame.display.flip()
    SCREEN.fill(BLACK)
    TEXT.draw(SCREEN)
    TEXT2.draw(SCREEN)

def main():
    clock.tick(5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit(); pygame.quit()
            if event.type == pygame.KEYUP: up(event)
        draw()

if __name__ == "__main__":
    main()
