from classes import*
import pygame
import math
import random
from pygame.locals import*

def main():
    pygame.init()
    #sets the display 
    table_image, table_rect = load_img('table.png')

    disp = pygame.display.set_mode(table_rect.size)
    pygame.display.set_caption('Air hockey')

    #creates the backgroud table 
    background = Background('table.png')
    background.image = background.image.convert()

    pygame.display.flip()

    #create a main menu option
    mainMenu = Background('menu.png')
    mainMenu.image = mainMenu.image.convert()
    

    #starts the game clock 
    clock = pygame.time.Clock()
    timeKeeper = Timer('digital-7.ttf', 60)
    

    #creating puck sprite and sestting it into a sprite group 
    puck = Puck(0, 0)
    puckSprite = pygame.sprite.RenderPlain(puck)

    #setting up the player and computer sprites and setting them to a group 
    player1 = Player()
    comp = Comp()

    player = pygame.sprite.RenderPlain(player1)
    compPlayer = pygame.sprite.RenderPlain(comp)

    compScore = Scores('digital-7.ttf', 70 , 0)
    playerScore = Scores('digital-7.ttf', 70, 0) 
    
    # final message
    message = pygame.font.Font('TESLA.ttf', 50)
    
    
    #flags to check what is going on in the game
    mainM = True 
    #accumulator for getting the recent coordinates of the computer. helps in
    #deciding the movement of the computer 
    coord = []
    #flag to check if a game is over 
    gameOver = False 
    while True:
        
        if mainM:
            #blits the main menu on the screen 
            disp.blit(mainMenu.image, (0,0))
            pygame.display.flip()
            #checks for the common events in the game 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif isClicked(120, 290, 130, 70):
                    mainM = False
                elif isClicked(540, 290, 130, 70):
                    pygame.quit() 
                    
    
            
            
        elif gameOver:
            #returns you to the main menu if the game is over. i.e 3 minutes have passed            
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif isClicked(120, 290, 130, 70):
                    print('its working')
                    #resetting all variables for another game 
                    mainM = False
                    gameOver = False 
                    puck.compScore = 0
                    puck.playerScore = 0
                    timeKeeper.min = 2
                    timeKeeper.seconds = 60
                    puck.rect.center = puck.area.center
                    
                #check to see if the user pressed the quit button    
                elif isClicked(540, 290, 130, 70):
                    pygame.quit()
                #check to see if player wins or computer wins or if it is a draw 
                if puck.compScore > puck.playerScore:
                    msg = message.render('Computer Wins', False, (0,0,0))
                elif puck.compScore == puck.playerScore:
                    msg = message.render('It is a draw!', False, (0,0,0))
                else:
                    msg = message.render('Player wins', False, (0,0,0))
                print(msg)
                disp.blit(mainMenu.image, (0,0))
                disp.blit(msg, (150, 200))
        else:
            #check to if game is over i.e 3 minutes have passed 
            if timeKeeper.min == -1:
                print('here') 
                gameOver = True 
                
                    
            # check to see if user has pressed the main menu button
            if isClicked(340, 0, 90, 50):
                mainM = True

            #updating the scores 
            compText = compScore.render(str(puck.compScore), False, (0,0,0))
            playerText = playerScore.render(str(puck.playerScore), False, (0,0,0))

            #checking the most recent coordinates of the computer 
            coord.append(comp.rect.center)
            disp.blit(background.image, (0, 0))

            #checking the updating the clock 
            timeElapsed = clock.tick(60)
            timeKeeper.update(timeElapsed)
            timeText= timeKeeper.displayTime() 
            
           
            #this flag is for the odd case where the computer gets stuck at a corner
            #with the puck 
            comp.stagnant = False 
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == MOUSEMOTION:
                    player1.mouseMove()
                
            #checks for the collision between puck and player sprite, handles its collision
            if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):

                (dx, dy) = pygame.mouse.get_rel()
                
                puck.angle = math.atan2(dy, dx)
                puck.speed = 30
            #checks for the collision between the computer and the puck     
            elif pygame.sprite.groupcollide(puckSprite, compPlayer, False, False, pygame.sprite.collide_circle) and len(coord) > 1:

                #determining the angle at which the puck should move after collsion
                #using basic trigonometry and vector math 
                dx = coord[-1][0] - coord[-2][0]
                dy = coord[-1][1] - coord[-2][1]

                if coord[-1][1] == coord[-2][1]:
    ##                puck.calcNewPos(puck.rect, math.pi, 30)
    ##                puck.angle = math.pi
                    comp.stagnant = True 
                else:
                    
                    puck.angle = math.atan2(dy, dx)
                    puck.speed = 30
     
            #checking to see if the puck is in the computer half, the computer
            #follows the puck only if it is in its half 
            if puck.courtHalf() == 'right': 
                comp.calculateNewPos(puck.rect.center)
            elif puck.courtHalf() == 'left':
                coord.clear()
            #places the puck back in the 
            if puck.goal:
                puck.goal = False 
                puck.rect.center = puck.area.center

          

            #blits all the objects on to the display every frame
            disp.blit(background.image, puck.rect, puck.rect) 
            disp.blit(background.image, player1.rect, player1.rect)
            disp.blit(background.image, comp.rect, comp.rect)
            disp.blit(compText, (550, 175))
            disp.blit(playerText, (220, 175))
            disp.blit(timeText, (340, 180))
            
         
            #updates the sprites 
            player.update()
            compPlayer.update() 
            puckSprite.update()
        
            
            player.draw(disp)
            puckSprite.draw(disp)
            compPlayer.draw(disp)
           
        
            pygame.display.flip()
main()