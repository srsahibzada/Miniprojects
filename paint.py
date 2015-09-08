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


class colorpicker():
	def __init__(self, screen, red,green,blue):
		self.screen = screen
		self.red = red
		self.green = green
		self.blue = blue
		

class paintmenu():
	'''menu has a paintbrush, shape drawer, fill bucket, color picker'''

class mainmenu():
	'''main menu has file (open, save, save as), edit (undo, redo)'''
#main 'game window' where the paint screen will be located

class colormenu():
	black = 0,0,0
	white = 255,255,255
	green = 0,255,0
	red = 255,0,0
	blue = 0,0,255
	sarahpink = 255,20,147
	colors = [black,white,green,red,blue,sarahpink]



class paintmodes():
	drawmode = False
	shapemode = False
	fillmode = False
	erasemode = False
	colorpickermode = True
	colormode = 0

def midpoint(a,b):
		print (((a[0]+b[0])/2) , ((a[1]+b[1])/2))
		return (((a[0]+b[0])/2) , ((a[1]+b[1])/2))

#def drawlines(surface,startpt,endpt,radius):



class paintwindow():

	def __init__(self):
			pygame.init()
			#mode = paintmodes.none
			screen = pygame.display.set_mode((1200,800))
			background = pygame.Surface(screen.get_size())
			background = background.convert()
			background.fill(white)
			paintmodes.colormode = 0
			color = colormenu.colors[0]
			pygame.display.set_caption("Sarah Paints")
			screen.blit(background,(0,0))
			pygame.display.flip()


			while 1:
				#for event in pygame.event.get():
				event = pygame.event.wait()
				if event.type == pygame.MOUSEBUTTONDOWN :
					paintmodes.drawmode = True
					pygame.draw.circle(screen,color,event.pos,7,0)
					index = event.pos
					pygame.display.flip()
					
					#background.fill(green)
					#screen.blit(screen,origin)
					#background.blit()
					print pygame.mouse.get_pressed()
				elif event.type == pygame.KEYDOWN:
					print "keypressed", pygame.key.name
					if event.key == pygame.K_a:
						color = colormenu.colors[0]
						print "recognized a change"
						pygame.display.flip()
					elif event.key == pygame.K_b:
						color = colormenu.colors[1]
						print "recognized a change"
						pygame.display.flip()
					elif event.key == pygame.K_c:
						color = colormenu.colors[2]
						print "recognized a change"
						pygame.display.flip()
					

				elif event.type == pygame.MOUSEBUTTONUP :
					paintmodes.drawmode = False
					#coordinates.finalcord = mouse.get_pos()
					pygame.display.flip()
					#background.fill(red)
					#screen.blit(background,(0,0))
					#pygame.display.flip()
					#print "lol"
				elif event.type == pygame.MOUSEMOTION:
					if paintmodes.drawmode == True:
						print color, "colorful"
						next = pygame.mouse.get_pos()
						pygame.draw.circle(screen,color,pygame.mouse.get_pos(),7,0)
						pygame.draw.lines(screen,color,True,(index,midpoint(index,next)),15)
						pygame.draw.circle(screen,color,next,7,0)
						pygame.draw.lines(screen,color,True,(midpoint(index,next),next),15)
						pygame.draw.circle(screen,color,midpoint(index,next),7,0)
						#pygame.draw.lines(screen,sarahpink,True,(index,midpoint(index,next),next),15)
						index = pygame.mouse.get_pos()
						pygame.display.flip()
				elif event.type == pygame.QUIT :
					return
				'''elif event.type == pygame.KEYDOWN:
					paintmodes.erasemode = True
					screen.fill(white)
					pygame.display.flip()
				elif event.type == pygame.KEYUP:
					paintmodes.erasemode = False #reset the eraser asap'''

					#pygame.display.flip()
				#prev = event.pos
				
def main():
	paintwindow()
	#paintmodes()
	
main()
