import pygame
from models.bullet import Proyectil

#variables globales
ancho = 940
alto = 480
listaEnemigo = []

class Jugador(pygame.sprite.Sprite):
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
		disparo = Proyectil(x,y,"D:\Imagenes/Diseño y creación/Pixel Art/gato.jpg", True)
		self.listaDisparo.append(disparo)

	def dibujar(self, superficie):
		superficie.blit(self.ImagenNave, self.rect)
