import pygame, sys, random
from pygame.locals import *
from random import randint

#variables globales
ancho = 940
alto = 480

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

class Proyectil(pygame.sprite.Sprite):
	
	def __init__(self, x, y, ruta, personaje):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenProyectil = pygame.image.load(ruta).convert()
		
		self.rect = self.ImagenProyectil.get_rect()
		self.velovidadDisparo = 1
		
		self.rect.top = y
		self.rect.left = x

		self.disparoPersojane = personaje

	def trayectoria(self):
		if self.disparoPersojane == True:
			self.rect.top -= self.velovidadDisparo
		else:
			self.rect.top += self.velovidadDisparo

	def dibujar(self, superficie):
		superficie.blit(self.ImagenProyectil, self.rect)

class Enemigo(pygame.sprite.Sprite):
	
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.Img1 = pygame.image.load("D:\Imagenes/Diseño y creación/Pixel Art/Cata_pixel_art_1.jpg").convert()
		self.Img2 = pygame.image.load("D:\Imagenes/Diseño y creación/Pixel Art/Cata_pixel_art_2.jpg").convert()
		self.Img3 = pygame.image.load("D:\Imagenes/Diseño y creación/Pixel Art/perro_03.jpg").convert()
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

	def dibujar(self, superficie):
		self.imagenEnemigo = self.listaImg[self.posImagen]
		superficie.blit(self.imagenEnemigo, self.rect)

	def comportamiento(self, tiempo):
		
		self._ataque()
		if self.tiempoCambio == tiempo:
			self.posImagen += 1
			self.tiempoCambio += 1

			if self.posImagen >= len(self.listaImg):
				self.posImagen = 0

	def _ataque(self):
		if (randint(0,100)<self.rangoDisparo):
			self._disparo()

	def _disparo(self):
		x,y = self.rect.center
		proyectilEnemigo = Proyectil(x,y,"D:\Imagenes/Diseño y creación/Pixel Art/perro_03.jpg", False)
		self.listaDisparo.append(proyectilEnemigo)

def SpaceInvader():
	pygame.init()
	ventana = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Chicken Invader")

	jugador = Jugador()
	enemigo = Enemigo(100,100)
	enJuego = True
	reloj = pygame.time.Clock()

	while True:
		ventana.fill((255,255,255))
		reloj.tick(60)
		tiempo = int(pygame.time.get_ticks()/1000)
		jugador.movimiento()

		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			if enJuego == True: #movimiento del jugador
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
		
		enemigo.comportamiento(tiempo)
		jugador.dibujar(ventana)
		enemigo.dibujar(ventana)

		if len(jugador.listaDisparo)>0: #disparo del jugador
			for x in jugador.listaDisparo:
				x.dibujar(ventana)
				x.trayectoria()
				
				if x.rect.top < 0:
					jugador.listaDisparo.remove(x)

		if len(enemigo.listaDisparo)>0: #disparo del enemigo
			for x in enemigo.listaDisparo:
				x.dibujar(ventana)
				x.trayectoria()
				
				if x.rect.top > 900:
					enemigo.listaDisparo.remove(x)
		pygame.display.update()

SpaceInvader()