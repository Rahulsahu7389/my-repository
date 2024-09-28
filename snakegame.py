import pygame
import random
pygame.init()

white = (255,255,255)
uv = (0,0,128)
uv4 = (255,0,0)
uv2 = (0,0,255)
uv3 = (55,55,55)
black = (0,0,0)
gamew = 1000
gameh = 1700

gamewin = pygame.display.set_mode((gamew,gameh))
def snakeplot(snakes,snk_list):
	for x,y in snk_list:
		pygame.draw.circle(gamewin,uv,[x,y],snakes,0)
	
def toxt(text,color,x,y):
	font = pygame.font.SysFont(None,65)
	screen_text = font.render(text, True, color)
	gamewin.blit(screen_text, [x,y])
	
def gameloop():
	######variables#####
	
	
	velocityx = 0
	velocityy= 0
	fps = 100
	choice = 0
	circlx = 70
	circly = 70
	initv = 8
	x2 = 200
	y2 = 200
	game_over = False
	sound = {}
	sound["point"] = pygame.mixer.Sound("/storage/emulated/0/Android/data/ru.iiec.pydroid3/files/Hardware rendering/assets/audio/point.ogg")
	sound["hit"] = pygame.mixer.Sound("/storage/emulated/0/Android/data/ru.iiec.pydroid3/files/Hardware rendering/assets/audio/hit.ogg")
	
	img = {}
	img["background"] = pygame.image.load("/storage/emulated/0/Android/data/ru.iiec.pydroid3/files/137074_light-green-backgrounds.jpg").convert_alpha()
	
	foodx = random.randint(gamew/2,gameh/2)
	foody = random.randint(gamew/2,gameh/2)
	#########
	pygame.display.set_caption("Snake Game")
	i = pygame.time.Clock()
	
	snk_list=[]
	snk = 1
	exit_game = False
	while not exit_game:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					exit_game = True
				if event.key == pygame.K_b:
					velocityx = initv
					velocityy = 0
				elif event.key == pygame.K_c:
					velocityx = - initv
					velocityy = 0
				elif event.key == pygame.K_v:
					velocityy = initv
					velocityx = 0
				elif event.key == pygame.K_RETURN:
					gameloop()
				elif event.key == pygame.K_g:
					velocityy  = -initv
					velocityx = 0
					
		circlx = circlx + velocityx
		circly = circly + velocityy
		if circlx <= 0 or circlx > gamew or circly < 0 or circly > gameh:
			#sound["hit"].play()
			game_over = True
			
		elif abs(circlx - foodx) < 13 and abs(circly - foody) < 13:
			#sound["point"].play()
			choice +=1
			snk += 5
			foodx = random.randint(gamew/2,gameh/2)
			foody = random.randint(gamew/2,gameh/2)
			
		head = []
		head.append(circlx)
		head.append(circly)
		snk_list.append(head)
		
		if len(snk_list) > snk :
			del snk_list[0]
		if head in snk_list[:-1]:
			game_over = True
			
		gamewin.fill(white)
		#gamewin.blit(img["background"],[0,0])
		toxt("Score " + str(choice),uv2,10,20)
		snakeplot(25,snk_list)
		food = pygame.draw.circle(gamewin,uv,[foodx,foody],25,0)
		if game_over == True:
			gamewin.fill(white)
			toxt("Game Over,if you want to quit enter [q]",uv3,200,200)
			toxt("Your score is " + str(choice),uv4,400,400)
			#for event in pygame.event.get():
				#			if event.type == pygame.KEYDOWN:
				#pygame.draw.rect(gamewin,uv,[circlx,circly], width = 25)
		i.tick(fps)
		pygame.display.update()
#for event in pygame.event.get():
	
	
gameloop()
