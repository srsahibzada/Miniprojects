import pygame
import pygame.mouse 
from pygame.event import *
from enum import enum
import random
'''PYGAME COLORS ARE STORED AS TUPLES!!!!!!!!'''
black = 0,0,0
white = 255,255,255
green = 0,255,0
red = 255,0,0
blue = 0,0,255
sarahpink = 255,20,147
origin = 0,0
grey = 190,190,190


class colorpicker():
	def __init__(self, screen,color):
		self.screen = screen
		self.color = color
		pygame.draw.rect(screen,color,0)
	def more_red():
		self.color = (self.color[0]+5, self.color[1], self.color[2])
	def more_blue():
		self.color = (self.color[0], self.color[1]+5, self.color[2])
	def more_green():
		self.color = (self.color[0]+5, self.color[1], self.color[2]+5)

class brush():
	minbrushsize = 10
	maxbrushsize = 300
	fill = 0 # max fill 
	brushsize = 10
	brushcolor = black
	origin = (600,600)
	def __init__(self,bs,bc,o,Surface):
		brushsize = bs
		brushcolor = bc
		origin = o
		pygame.draw.circle(Surface,bc,o,bs,brush.fill)
	def __init__(self,Surface):
		brushsize = brush.brushsize
		brushcolor = brush.brushcolor
		origin = brush.origin
		pygame.draw.circle(Surface,brushcolor,origin,brushsize,brush.fill)
	def increment_brush_size(self):
		if self.brushsize < self.maxbrushsize:
			self.brushsize += 5
	def decrement_brush_size(self):
		if self.brushsize > self.minbrushsize:
			self.brushsize -= 5

	def reset_origin(self,pos):
		brush.origin = pos

	def paint(self,init,Surface):
		pygame.draw.circle(Surface,self.brushcolor,init,self.brushsize,0)
		
	def set_color(self,color):
		brush.brushcolor = color

	def whereami(self,Surface):
		pygame.draw.circle(Surface,red,self.origin,self.brushsize,0)


class gamewindow():

	def __init__(self):
			pygame.init()
			#mode = paintmodes.none
			screen = pygame.display.set_mode((1200,800))
			background = pygame.Surface(screen.get_size())
			background = background.convert()
			background.fill(white)
			sketcher = brush(background)
			color = (random.randrange(256), random.randrange(256), random.randrange(256))
			sketcher.set_color(color)
			#colorful = colorpicker(background,color)
			pygame.display.set_caption("Etch a Sketch!")
			screen.blit(background,(0,0))
			pygame.display.flip()


			while 1:
				#for event in pygame.event.get():
				current = brush.origin
				sketcher.paint(current,screen)
				pygame.display.update()
				direction = pygame.key.get_pressed()
				if direction[pygame.K_UP] == True:
					sketcher.reset_origin((brush.origin[0],brush.origin[1]-1))
				elif direction[pygame.K_DOWN] == True:
					sketcher.reset_origin((brush.origin[0],brush.origin[1]+1))
				elif direction[pygame.K_LEFT] == True:
					sketcher.reset_origin((brush.origin[0]-1,brush.origin[1]))
				elif direction[pygame.K_RIGHT] == True:
					sketcher.reset_origin((brush.origin[0]+1,brush.origin[1]))

				for event in pygame.event.get():
					if event.type == pygame.QUIT :
						return
					elif event.type == pygame.KEYDOWN:
						sketcher.set_color(color)
						if event.key == pygame.K_a:
							sketcher.increment_brush_size()
							print sketcher.brushsize, " incremented brush radius"
						elif event.key == pygame.K_b:
							sketcher.decrement_brush_size()
							print sketcher.brushsize, " decremented brush radius"
						elif event.key == pygame.K_SPACE:
							bgcolor = (random.randrange(256), random.randrange(256), random.randrange(256))
							screen.fill(bgcolor)
							#pygame.display.flip()
						elif event.key == pygame.K_h:
							sketcher.whereami(screen)
							pygame.display.flip()


				
def main():
	gamewindow()
	#paintmodes()
	
main()
