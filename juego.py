import pygame, sys, random
from pygame.locals import *

#variables globales
ancho = 940
alto = 480

class NaveEspacial(pygame.sprite.Sprite):
	"""Clase para las naves"""

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenNave = pygame.image.load("D:\Imagenes/Diseño y creación/Pixel Art/alfredo.jpg").convert()

		self.rect = self.ImagenNave.get_rect()
		self.rect.centerx = ancho/2
		self.rect.centery = alto-10

		self.listaDisparo = []
		self.Vida = True
		self.velocidad = 20

	def mov_left(self):
		self.rect.left -= self.velocidad
		self.movimiento()

	def mov_top(self):
		self.rect.top -= self.velocidad
		self.movimiento()
	
	def mov_right(self):
		self.rect.right += self.velocidad
		self.movimiento()
	
	def mov_bottom(self):
		self.rect.bottom += self.velocidad
		self.movimiento()
	
	def movimiento(self):
		if self.Vida == True:
			if self.rect.left <=0:
				self.rect.left =0
			elif self.rect.right >= ancho:
				self.rect.right = ancho
			elif self.rect.top <=0:
				self.rect.top = 0
			elif self.rect.bottom >= alto+20:
				self.rect.bottom = alto+20
	
	def disparar(self, x, y):
		disparo = Proyectil(x,y)
		self.listaDisparo.append(disparo)

	def dibujar(self, superficie):
		superficie.blit(self.ImagenNave, self.rect)

class Proyectil(pygame.sprite.Sprite):
	
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenProyectil = pygame.image.load("D:\Imagenes/Diseño y creación/Pixel Art/gato.jpg").convert()
		
		self.rect = self.ImagenProyectil.get_rect()
		self.velovidadDisparo = 1
		
		self.rect.top = y
		self.rect.left = x

	def trayectoria(self):
		self.rect.top -= self.velovidadDisparo

	def dibujar(self, superficie):
		superficie.blit(self.ImagenProyectil, self.rect)

class Enemigo(pygame.sprite.Sprite):
	pass

def SpaceInvader():
	pygame.init()
	ventana = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Chicken Invader")

	jugador = NaveEspacial()

	enJuego = True
	reloj = pygame.time.Clock()

	while True:
		ventana.fill((255,255,255))
		reloj.tick(60)
		jugador.movimiento()

		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			if enJuego == True:
				if evento.type == pygame.KEYDOWN:
					if evento.key == K_LEFT or evento.key == ord('a'):
						jugador.mov_left()
					elif evento.key == K_RIGHT or evento.key == ord('d'):
						jugador.mov_right()
					elif evento.key == K_UP or evento.key == ord('w'):
						jugador.mov_top()
					elif evento.key == K_DOWN or evento.key == ord('s'):
						jugador.mov_bottom()
					elif evento.key == ord(' ') or evento.type == MOUSEBUTTONDOWN:
						x,y = jugador.rect.center
						jugador.disparar(x,y)
		
		jugador.dibujar(ventana)
		if len(jugador.listaDisparo)>0:
			for x in jugador.listaDisparo:
				x.dibujar(ventana)
				x.trayectoria()
				
				if x.rect.top < 0:
					jugador.listaDisparo.remove(x)
		pygame.display.update()

SpaceInvader()