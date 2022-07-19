# Lawson's breakout game
import pygame
import random
import time
from sys import exit
pygame.init()
pygame.mixer.pre_init(44100, 16 , 2 ,4096)
width, height = 436, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Break out")
red = [255, 0, 0]
blue = [0, 0, 255]
purple = [64, 0, 128]
orange = [255, 153, 0]
green = [102, 255, 153]
colours=[red, orange, purple, blue]
brick_width = 50
brick_height = 20
# bricks x and y position
brickx = 0
bricky = 65
paddle_width = 90
paddle_height = 10
paddle = pygame.Surface((paddle_width, paddle_height))
collided_sound = pygame.mixer.Sound("collide.wav")
failed_sound = pygame.mixer.Sound("failed.wav")
soft_sound = pygame.mixer.Sound("soft.wav")
power_up = pygame.mixer.Sound("powerup.wav")
paddle.fill("white")
# paddle x and y position
paddlex = width/2-paddle_width/2
paddley = height
paddle_rect = paddle.get_rect(bottomleft=(paddlex, paddley))
ball_radius = 9
clock = pygame.time.Clock()
brick = pygame.Surface((brick_width, brick_height))

# list to store our generated bricks
bricks = []
colour_list = []
# number to indicate our current level
number = 1
# a list of powerups
power_ups = ["Clone_balls!", "Empty!", "Life!","Weaken!"]
text_style = pygame.font.Font(None,30)
text_font = text_style.render("Level"+str(number), False, "white")
ball_xpos = width/2
ball_ypos = height-paddle_height-20

velx, vely = 4, 4
ball = pygame.Rect(ball_xpos, ball_ypos, 20, 20)
# variable determines if the ball should start moving
ball_move = False
# the life of the bricks from first row to bottom row
brick_lives = [4, 3, 2, 1]
# life of the player
life = 3
life_ball_width = 15
life_ball_spacing = life_ball_width+10
total_length = 65
game_on = True
win_message = text_style.render("YOU WIN!", True, "white")
win_rect = win_message.get_rect(center=(width/2, height/2))
class Brick:
    def __init__(self, block, xy, colour, lives):
        global brick_width
        global brick_height
        self.block = block
        self.colour = colour
        self.xy = xy
        self.lives = lives
        self.width = brick_width
        self.height = brick_height
        self.block = pygame.Surface((brick_width, brick_height))
        self.block_rect = self.block.get_rect(bottomleft= self.xy)

    def draw(self):
        self.block.fill(self.colour)
        screen.blit(self.block, self.block_rect)


# for a in range(4):
#     selected_colour = colours[a]
#     for b in range(8):
#         colour_list.append(selected_colour)
        

def init():
    global bricks
    bricks = []
    # generate rows
    for k in range(4):
        # generate columns
        for j in range(8):
            bricks.append(Brick(brick, (brickx+j*55, bricky+k*23), colours[k], 4-k))
            # print(k*7+k+j)
            #  or print(k+7*k+j)


init()


def select():
    for i in range(3):
        selected = random.choice(bricks).colour = green


clicked = 0

select()


def game_over():
    global game_on
    global life
    screen.fill("black")
    global clicked
    text = pygame.font.Font(None,70)
    message = text.render("Game Over", False, "white")
    message_rect = message.get_rect(center=(width/2, height/2-40))
    screen.blit(message, message_rect)
    pygame.draw.rect(screen, "white", (120, 250, 80, 30), 3, 50)
    retry = text_style.render("Retry", False, "White")
    retry_rect = retry.get_rect(center=(161, 265))
    home = text_style.render("Home", True, "White")
    home_rect = home.get_rect(center=(270, 265))
    screen.blit(retry, retry_rect)
    screen.blit(home, home_rect)
    mouse_pos = pygame.mouse.get_pos()
    if retry_rect.collidepoint(mouse_pos) and ev.type == pygame.MOUSEBUTTONDOWN:
        clicked += 1
    if clicked > 0:
        print("True")
        life = 3
        game_on = True
        init()
        select()


paused = False
pause_count = 0
timer = 60
initial_score = 0
final_score = 0


def pause():
    text3 = pygame.font.Font(None,50)
    message = text3.render("paused", True, "White")
    message_rect = message.get_rect(center=(width/2, height/2))
    screen.blit(message, message_rect)
class Bomb:
    def __init__(self, x , y):
        self.colour = "white"
        self.x = x
        self.y = y
        self.bomb_rect = pygame.Rect(self.x, self.y , 100, 100)
    def explode(self):
        self.colour = "white"
        pygame.draw.ellipse(screen, self.colour, self.bomb_rect )
    def fade(self):
        self.colour = "black"
        self.x = width/2
        self.y = height/2
    

def block(standby):
    if standby:
        rect = pygame.Rect(width/2-60, height/2+40,120,20)
        pygame.draw.rect(screen, "white",rect)
check = ""
show_message = True
score = 0
tolerance = 10
vel2x = 5
vel2y = 5
vel3x = 5
vel3y = 5
exploded = False
show_clone_balls = False
show_clone1 = False
show_clone2 = False
searching = True
bomb_timer = 0
touched = False
stay = False
while True:
    if searching:
        ball2 = pygame.Rect(ball.x , ball.y, 20, 20)
        ball3 = pygame.Rect(ball.x , ball.y , 20, 20)
        bomb  = Bomb(ball.x-40, ball.y-40)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                ball_move = True
            if ev.key == pygame.K_p:
                paused = True
                pause_count += 1
                game_on = False
                # continues the game if the player presses p for the second time
                if pause_count > 1:
                    paused = False
                    pause_count=0
                    game_on = True
            # if ev.key == pygame.K_s:
            #     show_clone1 = True
            #     show_clone2 = True
            #     searching = False
    if game_on:
        # moves the ball when space_bar is pressed
        if ball_move:
            ball.x -= velx 
            ball.y -= vely 
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT  and paddle_rect.x > 0:
                paddle_rect.x -= 4
            if ev.key == pygame.K_RIGHT and paddle_rect.right < width:
                paddle_rect.x += 4
            if ev.key == pygame.K_LEFT  and ball_move == False and paddle_rect.x > 0:
                ball.x -= 4
            if ev.key == pygame.K_RIGHT and ball_move == False and paddle_rect.right < width:
                ball.x += 4
            
        # slide mode
        # if ev.type == pygame.KEYUP:
        #     if ev.key == pygame.K_LEFT and paddle_rect.x > 0:
        #         paddle_rect.x -= 4
        #     if ev.key == pygame.K_RIGHT and paddle_rect.right < width:
        #         paddle_rect.x += 4

        screen.fill("black")
       
        # if show_clone_balls:
        if show_clone1:
            pygame.draw.ellipse(screen , "red", ball2)
            ball2.x -= vel2x
            ball2.y -= vel2y
        if show_clone2:
            pygame.draw.ellipse(screen , "red", ball3)
            ball3.x += vel3x
            ball3.y -= vel3y
        for i in range(life):
            pygame.draw.circle(screen, "red", (width-total_length+i*life_ball_spacing, 20), life_ball_width/2, 2)
    
        # loops through the bricks list to check for collision
        for brick in bricks:
            if ball.colliderect(brick.block_rect):
                if abs(ball.top - brick.block_rect.bottom) < tolerance and vely > 0:
                    vely = -vely
                if abs(ball.bottom - brick.block_rect.top) < tolerance and vely < 0:
                    vely = -vely
                if abs(ball.left - brick.block_rect.right) < tolerance and velx > 0:
                    velx = -velx
                if abs(ball.right - brick.block_rect.left) < tolerance and velx < 0:
                    velx = -velx
                brick.lives -= 1
                if brick.lives <= 0 or touched:
                    if brick.colour == green: 
                        timer = 60
                        check = random.choice(power_ups)
                        # print(check)
                        if check == "Life!":
                            power_up.play()
                            print(life) 
                            if life < 3:
                                life += 1
                        if check == "Clone_balls!":
                            power_up.play()
                            show_clone1 = True
                            show_clone2 = True
                            searching = False
                        if check == "Weaken!":
                            power_up.play()
                            exploded = True
                            searching= False
        
                    # remove the brick after it has been broken
                    bricks.pop(bricks.index(brick))
            if stay:
                block(stay)
            if exploded:
                bomb_timer += 1
                bomb.explode()
                if bomb.bomb_rect.colliderect(brick.block_rect):
                    print("touched")
                    brick.lives = 0
                if bomb_timer == 30:
                    exploded = False
                    bomb_timer = 0
                    touched = False
                    bomb.fade()
            if show_clone1:
                if ball2.colliderect(brick.block_rect):
                    if abs(ball2.top - brick.block_rect.bottom) < tolerance and vel2y > 0:
                        vel2y = -vel2y
                    if abs(ball2.bottom - brick.block_rect.top) < tolerance and vel2y < 0:
                        vel2y = -vel2y
                    if abs(ball2.left - brick.block_rect.right) < tolerance and vel2x > 0:
                        vel2x = -vel2x
                    if abs(ball2.right - brick.block_rect.left) < tolerance and vel2x < 0:
                        vel2x = -vel2x
                    brick.lives -= 1
                    if brick.lives <= 0:
                        if brick.colour == green: 
                            timer = 60
                            check = random.choice(power_ups)
                            # print(check)
                            if check == "Life!":
                                power_up.play()
                                print(life)
                                if life < 3:
                                    life += 1
                        if check == "Clone_balls!":
                            power_up.play()
                            show_clone1 = True
                            show_clone2 = True
                            searching = False
                        if check == "Weaken!":
                            power_up.play()
                            exploded = True
                            searching= False
                        # remove the brick after it has been broken
                        bricks.pop(bricks.index(brick))
            if show_clone2:
                if ball3.colliderect(brick.block_rect):
                    if abs(ball3.top - brick.block_rect.bottom) < tolerance and vel3y > 0:
                        vel3y = -vel3y
                    if abs(ball2.bottom - brick.block_rect.top) < tolerance and vel2y < 0:
                        vel3y = -vel3y
                    if abs(ball2.left - brick.block_rect.right) < tolerance and vel3x > 0:
                        vel3x = -vel3x
                    if abs(ball2.right - brick.block_rect.left) < tolerance and vel2x < 0:
                        vel3x = -vel3x
                    brick.lives -= 1
                    if brick.lives <= 0:
                        if brick.colour == green: 
                            timer = 60
                            check = random.choice(power_ups)
                            # print(check)
                            if check == "Life!":
                                power_up.play()
                                print(life)
                                if life < 3:
                                    life += 1
                        if check == "Clone_balls!":
                            power_up.play()
                            show_clone1 = True
                            show_clone2 = True
                            searching = False
                        if check == "Weaken!":
                            power_up.play()
                            exploded = True
                            searching= False
                       
                        # remove the brick after it has been broken
                        bricks.pop(bricks.index(brick))
        if ball.colliderect(paddle_rect):
        
            collided_sound.play()
            if abs(ball.bottom - paddle_rect.top) < tolerance and vely < 0:
                vely = -vely
            if abs(ball.left - paddle_rect.right) < tolerance and velx < 0:
                velx = -velx
            if abs(ball.right - paddle_rect.left) < tolerance and velx > 0:
                velx = -velx
        if show_clone1:
            if ball2.colliderect(paddle_rect):
                collided_sound.play()
                if abs(ball2.bottom - paddle_rect.top) < tolerance and vel2y < 0:
                    vel2y = -vel2y
                if abs(ball2.left - paddle_rect.right) < tolerance and vel2x < 0:
                    vel2x = -vel2x
                if abs(ball2.right - paddle_rect.left) < tolerance and vel2x > 0:
                    vel2x = -vel2x
        if show_clone2:
            if ball3.colliderect(paddle_rect):
                collided_sound.play()
                if abs(ball3.bottom - paddle_rect.top) < tolerance and vel3y < 0:
                    vel3y = -vel3y
                if abs(ball3.left - paddle_rect.right) < tolerance and vel3x < 0:
                    vel3x = -vel3x
                if abs(ball3.right - paddle_rect.left) < tolerance and vel3x > 0:
                    vel3x = -vel3x
        
        # display powerup collected
        if timer >= 0:
            if show_message:
                message = text_style.render(f"{check}", True, "white")
                message_rect = message.get_rect(center=(width/2, height/2))
                screen.blit(message, message_rect)
        if len(bricks) == 0:
            screen.blit(win_message, win_rect)
            ball_move = False
        # display the bricks on the screen
        for b in bricks:
            b.draw()
        screen.blit(text_font, (9, 10))
        screen.blit(paddle, paddle_rect)
        # draw the paddles ball
        pygame.draw.ellipse(screen, (255, 0, 0), ball)
        # check if the ball is going off-screen
        if ball.x < ball_radius or ball.x > width-20:
            velx = -velx
            soft_sound.play()
        if show_clone1:
            # check if the left clone ball is going off screen
            if ball2.x < ball_radius or ball2.x > width-20:
                vel2x = -vel2x
                soft_sound.play()
        if show_clone2:
            # check if the right clone ball is going off screen
            if ball3.x < ball_radius or ball3.x > width-20:
                vel3x = -vel3x
                soft_sound.play()
        # check if the ball is going off-screen 
        if ball.y < ball_radius:
            vely = -vely
        if ball.y > height:
            life -= 1
            failed_sound.play()
            ball_move = False
            # reset the ball and the paddle
            ball = pygame.Rect(ball_xpos, ball_ypos, 20, 20)
            paddle_rect = paddle.get_rect(bottomleft=(paddlex, paddley))
        # check if the left clone ball is going off screen
        if ball2.y < ball_radius:
            vel2y = -vel2y
        if ball2.y > height:
            show_clone1 = False
        # check if the right clone ball is going off screen
        if ball3.y < ball_radius:
            vel3y = -vel3y
        if ball3.y > height:
            show_clone2 = False
        if show_clone1 == False and show_clone2 == False:
            searching = True
        # switch to game over screen when life is zero
        if life <= 0:
            game_on = False
            show_clone1 = False
            show_clone2 = False
            clicked = 0
            # pygame.quit()
            # exit()
    elif paused:
        pause()
    else:
        game_over()
    timer -= 1
    clock.tick(60)
    pygame.display.update()

