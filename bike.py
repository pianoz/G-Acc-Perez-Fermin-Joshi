import socket
import pygame


# game variables
self = pygame.init()
rbound = 1000
hbound = 1000
screen = pygame.display.set_mode((rbound, hbound))
imagemap = pygame.image.load('map.png')


# socket variables
UDP_IP = "127.0.0.1"
UDP_PORT = 12000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))


# Game code here, this currently works with keys for testing.

def game(self, screen):

    dir=0
    # little cursor images
    imageleft = pygame.image.load('left.png')
    imageright = pygame.image.load('right.png')
    imageup = pygame.image.load('up.png')
    imagedown = pygame.image.load('down.png')
    imagemap = pygame.image.load('map.png')

    imagex = 500
    imagey = 500

    image_direction_value = 0;

    while 1:

        'active keypressing'
        keys = pygame.key.get_pressed()

        'moving left'
        if keys[pygame.K_a] or keys[pygame.K_LEFT] or dir == 1:
            image_direction_value = 0
            'left boundary and movement'
            if imagex > 0:
                imagex = imagex - 3

        'moving right'
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] or dir == 2:
            image_direction_value = 1
            'setting boundaries and then movement'
            if imagex < rbound:
                imagex = imagex + 3

        'moving up'
        if keys[pygame.K_w] or keys[pygame.K_UP] or dir == 3:
            image_direction_value = 2
            if imagey < rbound:
                imagey = imagey - 3

        'moving down'
        if keys[pygame.K_s] or keys[pygame.K_DOWN] or dir == 4:
            image_direction_value = 3
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
        if image_direction_value == 0:
            screen.blit(imageleft, (imagex, imagey))
        if image_direction_value == 1:
            screen.blit(imageright, (imagex, imagey))
        if image_direction_value == 2:
            screen.blit(imageup, (imagex, imagey))
        else:
            screen.blit(imagedown, (imagex, imagey))
        pygame.display.flip()

        # listen for Wekinator
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        # print(data,"\n",data[20], " ",data[21])

        # DATA COMES IN FROM 20 & 21, using classifiers, you can get distinct sums which allow diferentiation
        # ... between 1,2,3,4. If you change this to continuous, then you will have to change this.
        tempsum = data[20] + data[21]

        if tempsum == 191:
            # result 1, classifier 1, direction left
            dir = 1

        if tempsum == 64:
            # result 2, classifier 2 direction right
            dir = 2

        if tempsum == 128:
            # result 3, classifier 3, direction up
            dir = 3

        if tempsum == 192:
            # result 4, classifier 4, direction down
            dir = 4

game(self, screen)
