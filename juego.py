import pygame, sys, random
from pygame.locals import *

#variables globales
ancho = 940
alto = 480




class NaveEspacial(pygame.sprite.Sprite):
	"""Clase para las naves"""

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenNave = pygame.image.load("imagenes/cervezas.png")

		self.rect = self.ImagenNave.get_rect()
		self.rect.centerx = ancho/2
		self.rect.centery = alto-10

		self.listaDisparo = []
		self.Vida = True
		self.velocidad = 20

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
	
	def disparar(self,x,y): 
		miProyectil =  Proyectil(x,y)
		self.listaDisparo.append(miProyectil)

	def dibujar(self, superficie):
		superficie.blit(self.ImagenNave, self.rect)

class Proyectil(pygame.sprite.Sprite):
	
	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)

		self.ImagenProyectil = pygame.image.load("imagenes/corazon.png")
		
		self.rect = self.ImagenProyectil.get_rect()
		self.velovidadDisparo = 1
		
		self.rect.top = posy
		self.rect.left = posx

	def trayectoria(self):
		self.rect.top -= self.velovidadDisparo

	def dibujar(self, superficie):
		superficie.blit(self.ImagenProyectil, self.rect)

def SpaceInvader():
	pygame.init()
	ventana = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Chicken Invader")

	jugador = NaveEspacial()
	proyectil = Proyectil(ancho/2, alto)

	enJuego = True
	while True:
		
		ventana.fill((255,255,255))
		jugador.movimiento()
		proyectil.trayectoria()

		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			if enJuego == True:
				if evento.type == pygame.KEYDOWN:
					if evento.key == K_LEFT or evento.key == ord('a'):
						jugador.rect.left -= jugador.velocidad
					elif evento.key == K_RIGHT or evento.key == ord('d'):
						jugador.rect.right += jugador.velocidad
					elif evento.key == K_UP or evento.key == ord('w'):
						jugador.rect.top -= jugador.velocidad
					elif evento.key == K_DOWN or evento.key == ord('s'):
						jugador.rect.bottom += jugador.velocidad
					elif evento.key == ord(' '):
						x,y = jugador.rect.center
						jugador.disparar(x,y)
		
		proyectil.dibujar(ventana)
		jugador.dibujar(ventana)
		if len(jugador.listaDisparo)>0:
			for x in jugador.listaDisparo:
				x.dibujar(ventana)
				x.trayectoria()

				if x.rect.top<0:
					jugador.listaDisparo.remove(x)
		pygame.display.update()

SpaceInvader()