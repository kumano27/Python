import pygame
import math

def sgn(a):
    return 1 if a > 0 else -1

width  = 640
height = 480
white  = (255, 255, 255)
red    = (255,   0,   0)
yellow = (255, 255,   0)
green  = (  0, 255,   0)
blue   = (  0,   0, 255)
colortable = [red,yellow,green]

pygame.init()

screen = pygame.display.set_mode((width,height))
myfont = pygame.font.Font(None, 64)
myclock = pygame.time.Clock()
br = 10
paddlew = 96
paddleh = 16
blockw = 48
blockh = 24
endflag = 0

while endflag == 0:
	ballx = width / 2
	bally = height - 170
	bx1 = 2
	by1 = -2.5
	x = width / 2
	y = height - 64
	paddle = pygame.Rect(x - (paddlew / 2),y - (paddleh / 2), paddlew, paddleh)
	blocks = []
	for i in range(50):
		x = (i % 10) * (blockw + 4) + 64
		y = int(i / 10) * (blockh + 4) + 64
		blocks.append(pygame.Rect(x, y, blockw, blockh))
	gameover = 0
	while endflag == 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: endflag = 1
		press = pygame.key.get_pressed()
		x = paddle.centerx
		if(press[pygame.K_LEFT ]): x -= 8
		if(press[pygame.K_RIGHT]): x += 8
		if x >= (paddlew / 2) and x <= (width - (paddlew / 2)):
			paddle.centerx = x
		x = ballx + bx1
		y = bally + by1
		if x < br or x > (width - br): bx1 = -bx1
		if y < br: by1 = -by1
		if y > height: gameover += 1
		dx = paddle.centerx - x
		dy = paddle.centery - y
		if dy == 0: dy = 1
		if abs(dx) < (paddlew / 2 + br) and abs(dy) < (paddleh / 2 + br):
			if abs(dx /dy) > (paddlew / paddleh):
				bx1 = -bx1
				ballx = paddle.centerx - sgn(dx) * (paddlew / 2 + br)
			else:
				bx1 = -dx / 10
				by1 = -by1
				bally = paddle.centery - sgn(dy) * (paddleh / 2 + br)
		for block in blocks:
			dx = block.centerx - x
			dy = block.centery - y
			if dy == 0: dy = 1
			if abs(dx) < (blockw / 2 + br) and abs(dy) < (blockh / 2 + br) :
				if abs(dx / dy) > (blockw / blockh):
					bx1 = -bx1
					ballx = block.centerx - sgn(dx) * (blockw / 2 + br)
				else:
					by1 = -by1
					bally = block.centery - sgn(dy) * (blockh / 2 + br)
				blocks.remove(block)
				break
		ballx += bx1
		bally += by1
		screen.fill(blue)
		for block in blocks:
			color = colortable[int(block.y / 28) % 3]
			pygame.draw.rect(screen, color, block)
		pygame.draw.rect(screen, white, paddle)
		pygame.draw.circle(screen, white, (int(ballx), int(bally)), br)
		if gameover > 0:
			imagetext = myfont.render("GAME OVER", True, white)
			screen.blit(imagetext, (180, 300))
			if gameover > 200: break
		myclock.tick(60)
		pygame.display.flip()