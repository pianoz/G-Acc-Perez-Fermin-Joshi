
import socket
import pygame
import math


self = pygame.init()
rbound = 1000
hbound = 1000
screen = pygame.display.set_mode((rbound, hbound))
imagemap = pygame.image.load('map.png')
dir = 0;


UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


# Game code here, this currently works with keys for testing.

def main(self, screen):
    imageleft = pygame.image.load('left.png')
    imageright = pygame.image.load('right.png')
    imageup = pygame.image.load('up.png')
    imagedown = pygame.image.load('down.png')
    imagemap = pygame.image.load('map.png')

    imagex = 500
    imagey = 500

    dval = 0;

    while 1:



        'active keypressing'
        keys = pygame.key.get_pressed()

        'moving left'
        if keys[pygame.K_a] or keys[pygame.K_LEFT] or dir == 1:
            dval = 0
            'left boundary and movement'
            if imagex > 0:
                imagex = imagex - 3

        'moving right'
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] or dir == 2:
            dval = 1
            'setting boundaries and then movement'
            if imagex < rbound:
                imagex = imagex + 3

        'moving up'
        if keys[pygame.K_w] or keys[pygame.K_UP] or dir == 3:
            dval = 2
            if imagey < rbound:
                imagey = imagey - 3

        'moving down'
        if keys[pygame.K_s] or keys[pygame.K_DOWN] or dir == 4:
            dval = 3
            if imagey > 0:
                imagey = imagey + 3

        for event in pygame.event.get():

            'quit statements'
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        'player/map draw and refresh'
        screen.blit(imagemap, (0, 0))
        if dval == 0:
            screen.blit(imageleft, (imagex, imagey))
        if dval == 1:
            screen.blit(imageright, (imagex, imagey))
        if dval == 2:
            screen.blit(imageup, (imagex, imagey))
        else:
            screen.blit(imagedown, (imagex, imagey))
        pygame.display.flip()

        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        if 
        print("received message:", data)

main(self,screen)

