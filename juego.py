import pygame, sys, random
from models.player import Jugador
from models.enemy import Enemigo
from pygame.locals import *


#variables globales
ancho = 940
alto = 480
listaEnemigo = []
imagenJugador = ["./img/player.jpg"]

def cargarEnemigos():
	enemigo = Enemigo(100,100,400)
	listaEnemigo.append(enemigo)

def SpaceInvader():
	pygame.init()
	ventana = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Chicken Invader")

	jugador = Jugador(imagenJugador[0])
	cargarEnemigos()
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
		
		jugador.dibujar(ventana)

		if len(jugador.listaDisparo)>0: #disparo del jugador
			for x in jugador.listaDisparo:
				x.dibujar(ventana)
				x.trayectoria()
				
				if x.rect.top < 0:
					jugador.listaDisparo.remove(x)
				else:
					for enemigo in listaEnemigo:
						if x.rect.colliderect(enemigo.rect):
							listaEnemigo.remove(enemigo)
							jugador.listaDisparo.remove(x)

		if len(listaEnemigo) > 0:
			for enemigo in listaEnemigo:
				enemigo.comportamiento(tiempo)
				enemigo.dibujar(ventana)

				if enemigo.rect.colliderect(jugador.rect):
					print('te llenaron de mierda y perdiste ameo')

				if len(enemigo.listaDisparo)>0: #disparo del enemigo
					for x in enemigo.listaDisparo:
						x.dibujar(ventana)
						x.trayectoria()
						
						if x.rect.colliderect(jugador.rect):
							print('te cago un pajaro')

						if x.rect.top > 900:
							enemigo.listaDisparo.remove(x)
						else:
							for disparo in jugador.listaDisparo:
								if x.rect.colliderect(disparo.rect):
									jugador.listaDisparo.remove(disparo)
									enemigo.listaDisparo.remove(x)
		
		pygame.display.update()

SpaceInvader()