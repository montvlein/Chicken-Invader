import pygame

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
