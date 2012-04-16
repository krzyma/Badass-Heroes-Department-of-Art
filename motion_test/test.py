import pygame

screen = pygame.display.set_mode((640,480))
running = True

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

scale = 2
spritesheet = pygame.image.load("../spritesheets/npc-zombie.png").convert_alpha()
spritesheet = pygame.transform.scale(spritesheet, (128*scale, 128*scale))
#spritesheet.set_colorkey((255,255,255));
ss_pants = pygame.image.load("../spritesheets/tights_01.png")
ss_pants = pygame.transform.scale(ss_pants, (128*scale, 128*scale))
ss_armor = pygame.image.load("../spritesheets/breastplate_01.png")
ss_armor = pygame.transform.scale(ss_armor, (128*scale, 128*scale))
ss_hair = pygame.image.load("../spritesheets/headgear_01.png")
ss_hair = pygame.transform.scale(ss_hair, (128*scale, 128*scale))

show_armor = False
show_pants = True
show_hair = True

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert_alpha()
    image = pygame.transform.scale(image, (128*scale, 160*scale))
    #image.set_colorkey((255,0,255));
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_y in range(0, image_height/height):
        #line = []
        #tile_table.append(line)
        for tile_x in range(0, image_width/width):
            rect = (tile_x*width, tile_y*height, width, height)
            tile_table.append(image.subsurface(rect))
    return tile_table

def load_shadows_table(filename, width, height):
    image = pygame.image.load(filename).convert_alpha()
    image = pygame.transform.scale(image, (128*scale, 160*2*scale))
    #image.set_colorkey((255,0,255));
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_y in range(0, image_height/height):
        #line = []
        #tile_table.append(line)
        for tile_x in range(0, image_width/width):
            rect = (tile_x*width, tile_y*height, width, height)
            tile_table.append(image.subsurface(rect))
    return tile_table

tileset = load_tile_table("../tilesets/tileset2.png", 32*scale, 32*scale)
shadows = load_shadows_table("../tilesets/tileset2-shadows.png", 32*scale, 64*scale)

tilemap = [[6, 0, 0, 0, 0, 0, 6, 0, 6, 0],
[12, 0, 1, 5, 5, 5, 9, 0, 12, 0],
[0, 0, 6, 0, 0, 0, 6, 0, 0, 0],
[5, 5, 10, 2, 0, 0, 7, 5, 8, 5],
[0, 0, 0, 7, 5, 5, 3, 0, 6, 0],
[5, 2, 0, 6, 0, 0, 0, 0, 6, 0],
[0, 12, 0, 6, 0, 1, 11, 0, 4, 5],
[0, 0, 0, 6, 0, 6, 0, 0, 0, 0]
]

tilex = 0
tiley = 0
for tiley in range(8):
	for tilex in range(10):
		#background.blit(tileset[16], (tilex*32*scale, tiley*32*scale))
		background.blit(tileset[tilemap[tiley][tilex]-1], (tilex*32*scale, tiley*32*scale))
		#background.blit(shadows[tilemap[tiley][tilex]-1], (tilex*32*scale, tiley*32*scale))


clock = pygame.time.Clock()
frame = 0;
direction = 1;
x = 320
y = 320
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

