import pygame
from models.bullet import Proyectil
from random import randint

#variables globales
ancho = 940
alto = 480
listaEnemigo = []

class Enemigo(pygame.sprite.Sprite):
	
	def __init__(self, x, y, distancia):
		pygame.sprite.Sprite.__init__(self)
		self.Img1 = pygame.image.load("./img/enemy_1.jpg").convert()
		self.Img2 = pygame.image.load("./img/enemy_1.jpg").convert()
		self.listaImg = [self.Img1, self.Img2]
		self.posImagen = 0

		self.imagenEnemigo = self.listaImg[self.posImagen]
		self.rect = self.imagenEnemigo.get_rect()
		
		self.listaDisparo = []
		self.velocidad = 5
		self.rect.top = y
		self.rect.left = x

		self.rangoDisparo = 5
		self.tiempoCambio = 1

		self.limiteDerecha = x + distancia
		self.limiteIzquierda = x - distancia

		self.derecha = True
		self.contador = 0
		self.Maxdescenso = self.rect.top+40

	def dibujar(self, superficie):
		self.imagenEnemigo = self.listaImg[self.posImagen]
		superficie.blit(self.imagenEnemigo, self.rect)

	def comportamiento(self, tiempo):
		self.__movimientos()
		self.__ataque()
		if self.tiempoCambio == tiempo:
			self.posImagen += 1
			self.tiempoCambio += 1

			if self.posImagen >= len(self.listaImg):
				self.posImagen = 0

	def __ataque(self):
		if (randint(0,100)<self.rangoDisparo):
			self.__disparo()

	def __disparo(self):
		x,y = self.rect.center
		proyectilEnemigo = Proyectil(x,y,"./img/bulletDog.jpg", False)
		self.listaDisparo.append(proyectilEnemigo)

	def __movimientos(self):
		if self.contador < 3:
			self.__movimientoLateral()
		else:
			self.__movimientoDescenso()

	def __movimientoLateral(self):
		if self.derecha == True:
			self.rect.left += self.velocidad
			if self.rect.left > self.limiteDerecha:
				self.derecha = False
				self.contador += 1
		else:
			self.rect.left -= self.velocidad
			if self.rect.left < self.limiteIzquierda:
				self.derecha = True

	def __movimientoDescenso(self):
		if self.Maxdescenso == self.rect.top:
			self.contador = 0
			self.Maxdescenso = self.rect.top + 40
		else:
			self.rect.top += 1
