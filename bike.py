import pygame
import argparse
import math
from pythonosc import dispatcher
from pythonosc import osc_server

self = pygame.init()
rbound = 1000
hbound = 1000
screen = pygame.display.set_mode((rbound, hbound))
imagemap = pygame.image.load('map.png')

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
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dval = 0
            'left boundary and movement'
            if imagex > 0:
                imagex = imagex - 3

        'moving right'
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dval = 1
            'setting boundaries and then movement'
            if imagex < rbound:
                imagex = imagex + 3

        'moving up'
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dval = 2
            if imagey < rbound:
                imagey = imagey - 3

        'moving down'
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
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


# This is code to listen to osc data, I'm having trouble with the following part, and I'm not
# ...sure if it is due to the IP i've given it, or if it is something deeper. Some help would be
# ...greatly appreaciated.

def print_volume_handler(unused_addr, args, volume):
    print("[{0}] ~ {1}".format(args[0], volume))


def print_compute_handler(unused_addr, args, volume):
    try:
        print("[{0}] ~ {1}".format(args[0], args[1](volume)))
    except ValueError:
        pass


# Replace ip and port in here, this calls the game and makes sure messages come in,

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=12000, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/filter", print)
    dispatcher.map("/volume", print_volume_handler, "Volume")
    dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    main(self, screen)
    server.serve_forever()


