import pygame 
from random import randrange


RES = 700
SIZE = 50

x,y = randrange(0,RES- SIZE,SIZE),randrange(0,RES - SIZE,SIZE)
apple = randrange(0,RES - SIZE,SIZE),randrange(0,RES - SIZE,SIZE)
lenght = 1
snake = [(x,y)]
dx,dy = 0,0
fps =8
score = 0
pygame.init()
sc = pygame.display.set_mode([RES,RES])
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
dirs = {"UP":True,"DOWN":True,"LEFT":True,"RIGHT":True,}
myfont = pygame.font.Font('images/txt.ttf', 50)
def check_collision(snake):
    return len(snake) != len(set(snake))
gameplay =True
running = True
while running:
    sc.fill(pygame.Color("black"))
    score_text = myfont.render("Score:"+str(score),False,"White")
    sc.blit(score_text,(10,10))
    [pygame.draw.rect(sc,pygame.Color("green"),(i,j,SIZE-2,SIZE-2))for i,j in snake]
    [pygame.draw.rect(sc,pygame.Color("red"),(*apple,SIZE,SIZE))for i,j in snake]
    
    
    x += dx *SIZE
    y += dy * SIZE
    snake.append((x,y))
    if snake[-1] == apple:
        apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
        lenght += 1
        fps -= 0.1
        score +=10
    else:
        snake = snake[-lenght:]


    x  %= RES
    y %= RES

        
    pygame.display.flip()

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False


        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and dirs["UP"]:
            dx, dy = 0, -1
            dirs.update({"UP": True, "DOWN": False, "LEFT": True, "RIGHT": True})
        if key[pygame.K_DOWN] and dirs["DOWN"]:
            dx, dy = 0, 1
            dirs.update({"UP": False, "DOWN": True, "LEFT": True, "RIGHT": True})
        if key[pygame.K_LEFT] and dirs["LEFT"]:
            dx, dy = -1, 0
            dirs.update({"UP": True, "DOWN": True, "LEFT": True, "RIGHT": False})
        if key[pygame.K_RIGHT] and dirs["RIGHT"]:
            dx, dy = 1, 0
            dirs.update({"UP": True, "DOWN": True, "LEFT": False, "RIGHT": True})
        

    if x == 0 and dx == -1 :
        x = RES- SIZE

    elif  x == RES - SIZE and dx == 1:
        x= 0

    elif y == 0 and dy == -1 :
        y = RES - SIZE

    elif y == RES - SIZE and dy == 1:
        y = 0
    if check_collision(snake):
        running = False
        print("Sen uduzdun")
    

    