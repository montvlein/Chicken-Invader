import pygame
from models.bullet import Proyectil

#variables globales
ancho = 940
alto = 480
listaEnemigo = []

class Jugador(pygame.sprite.Sprite):
	"""Clase para las naves"""

	def __init__(self, imagenJugador):
		pygame.sprite.Sprite.__init__(self)
		self.Imagen = pygame.image.load(imagenJugador).convert()

		self.rect = self.Imagen.get_rect()
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
		disparo = Proyectil(x,y,"./img/bulletCat.jpg", True)
		self.listaDisparo.append(disparo)

	def dibujar(self, superficie):
		superficie.blit(self.Imagen, self.rect)
