import pygame

screen = pygame.display.set_mode((640,480))
running = True

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

scale = 2
spritesheet = pygame.image.load("../base/walking.png")
spritesheet = pygame.transform.scale(spritesheet, (128*scale, 128*scale))

ss_pants = pygame.image.load("../base/pants.png")
ss_pants = pygame.transform.scale(ss_pants, (128*scale, 128*scale))
ss_armor = pygame.image.load("../base/armor.png")
ss_armor = pygame.transform.scale(ss_armor, (128*scale, 128*scale))
ss_hair = pygame.image.load("../base/hair.png")
ss_hair = pygame.transform.scale(ss_hair, (128*scale, 128*scale))

show_armor = False
show_pants = True
show_hair = True

clock = pygame.time.Clock()
frame = 0;
direction = 1;
x = 320
y = 240
moving = False
pygame.key.set_repeat()
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False

	pressed = pygame.key.get_pressed()

	if pressed[pygame.K_1]:
		show_hair = not show_hair
	if pressed[pygame.K_2]:
		show_armor = not show_armor
	if pressed[pygame.K_3]:
		show_pants = not show_pants
	if pressed[pygame.K_UP]:
		moving = True
		y -= 5
		direction = 0
	elif pressed[pygame.K_DOWN]:
		moving = True
		y += 5
		direction = 1
	elif pressed[pygame.K_LEFT]:
		moving = True
		x -= 5
		direction = 2
	elif pressed[pygame.K_RIGHT]:
		moving = True
		x += 5
		direction = 3
	else:
		moving = False

	if moving:
		frame += 1
		if frame >= 4:
			frame = 0

	screen.blit(background, (0, 0))
	screen.blit(spritesheet.subsurface(frame*32*scale,direction*32*scale,32*scale,32*scale), (x,y))
	if show_armor:
		screen.blit(ss_armor.subsurface(frame*32*scale,direction*32*scale,32*scale,32*scale), (x,y))
	if show_pants:
		screen.blit(ss_pants.subsurface(frame*32*scale,direction*32*scale,32*scale,32*scale), (x,y))
	if show_hair:
		screen.blit(ss_hair.subsurface(frame*32*scale,direction*32*scale,32*scale,32*scale), (x,y))
	pygame.display.flip()
	clock.tick(6)

