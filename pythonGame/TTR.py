import pygame, sys
pygame.init()

##sets the window size to 800x600px
display_width = 800
display_height = 600

##easy access to colors
black = (0,0,0)
white = (255,255,255)
red =   (255,0,0)
green = (0,255,0)
blue =  (0,0,255)

##makes the screen as wide and tall as above variables, makes a white background, adds TTR title, and starts a clock
screen = pygame.display.set_mode([display_width,display_height])
screen.fill(white)
pygame.display.set_caption("TTR")
clock = pygame.time.Clock()

##loads images to act as the draw deck
whiteTrainImg = pygame.image.load('whiteTrain.png')
blackTrainImg = pygame.image.load('blackTrain.png')

numCards = 0

##draws the hitboxes for the white and black card draw piles
blackDeck = pygame.draw.rect(screen, (255, 255, 255),(display_width * 0.05,display_height * 0.9, 50, 50))
whiteDeck = pygame.draw.rect(screen, (255, 255, 255),(display_width * 0.15,display_height * 0.9, 50, 50))

##draws the black and white train card on the card piles over the hitboxes
screen.blit(whiteTrainImg,(display_width * 0.05,display_height * 0.9))
screen.blit(blackTrainImg,(display_width * 0.15,display_height * 0.9))

##card class, holds color
class Card:

    def __init__(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color = color

##initilized the hand array and keeps track of the card index
handCards = []
cardIndex = 0

##main while loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if len(handCards) >= 14:
                print('There are 14 cards in your hand, you can not draw any more!')
                
            elif blackDeck.collidepoint(pos):
                handCards.append(Card('black'))
                print('added black card to your hand')
                screen.blit(blackTrainImg,(display_width * 0.05 + (50 * cardIndex),display_height * 0.05))
                cardIndex+=1
                
            elif whiteDeck.collidepoint(pos):
                print('added white card to your hand')
                handCards.append(Card('white'))
                screen.blit(whiteTrainImg,(display_width * 0.05 + (50 * cardIndex),display_height * 0.05))
                cardIndex+=1
                
    pygame.display.update()
    clock.tick(10)
    
pygame.quit()
quit()

