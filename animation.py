import sys, pygame, settings
screen = pygame.display.set_mode((1024, 768))

def jump(player, reverse):
    images = [pygame.image.load(f"./assets/Samurai/jump{i}.png") for i in range(1, 7)]
    images.append(pygame.image.load("./assets/Samurai/idle1.png"))
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for frame in frames:
        match frame:
            case 0:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 1:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 2:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 3:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 4:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 5:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 6:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 7:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 8:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 9:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 10:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 11:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 12:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 13:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 14:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 15:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 16:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 17:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 18:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 19:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 20:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 21:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 22:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 23:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 24:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 25:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 26:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 27:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 28:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 29:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 30:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 31:
                player.image = pygame.transform.flip(images[6], reverse, False)
            case 32:
                player.image = pygame.transform.flip(images[6], reverse, False)
            case 33:
                player.image = pygame.transform.flip(images[6], reverse, False)
            case 34:
                player.image = pygame.transform.flip(images[6], reverse, False)
            case 35:
                player.image = pygame.transform.flip(images[6], reverse, False)
            case 36:
                player.image = pygame.transform.flip(images[7], reverse, False)
            case 37:
                player.image = pygame.transform.flip(images[7], reverse, False)
            case 38:
                player.image = pygame.transform.flip(images[7], reverse, False)
            case 39:
                player.image = pygame.transform.flip(images[len(images)], reverse, False)

        yield

def special3(player, reverse):
    images = [pygame.image.load(f"./assets/Samurai/thirdspecial{i}.png") for i in range(1, 6)]
    images.append(pygame.image.load("./assets/Samurai/attack1.png"))
    images.append(pygame.image.load("./assets/Samurai/idle1.png"))
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for frame in frames:
        match frame:
            case 0:
                # hitbox info here, for example, (220,200)
                jumpable = False # So that the player can jump cancel the animation at a certain point
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 1:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 2:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 3:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 4:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 5:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 6:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 7:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 8:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 10:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 11:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 12:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 13:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 15:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 16:
                player.image = pygame.transform.flip(images[6], reverse, False)
        yield


def special2(player, reverse):
    images = [pygame.image.load(f"./assets/Samurai/secondspecial{i}.png") for i in range(1, 8)]
    images.append(pygame.image.load("./assets/Samurai/attack1.png"))
    images.append(pygame.image.load("./assets/Samurai/idle1.png"))
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for frame in frames:
        match frame:
            case 0:
                # hitbox info here, for example, (220,200)
                jumpable = False # So that the player can jump cancel the animation at a certain point
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 1:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 2:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 3:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 4:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 5:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 6:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 7:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 8:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 10:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 11:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 12:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 13:
                player.image = pygame.transform.flip(images[6], reverse, False)
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[6], reverse, False)
            case 15:
                player.image = pygame.transform.flip(images[7], reverse, False)
            case 16:
                player.image = pygame.transform.flip(images[8], reverse, False)
        yield


def special1(player, reverse):
    images = [pygame.image.load(f"./assets/Samurai/special{i}.png") for i in range(1, 5)]
    images.append(pygame.image.load("./assets/Samurai/attack1.png"))
    images.append(pygame.image.load("./assets/Samurai/idle1.png"))
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for frame in frames:
        match frame:
            case 0:
                # hitbox info here, for example, (220,200)
                jumpable = False # So that the player can jump cancel the animation at a certain point
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 1:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 2:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 3:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 4:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 5:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 6:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 7:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 8:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 10:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 11:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 12:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 13:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 15:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 16:
                player.image = pygame.transform.flip(images[5], reverse, False)
        yield

def attack3(player, reverse):
    images = [pygame.image.load(f"./assets/Samurai/thirdattack{i}.png") for i in range(1, 5)]
    images.append(pygame.image.load("./assets/Samurai/attack1.png"))
    images.append(pygame.image.load("./assets/Samurai/idle1.png"))
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for frame in frames:
        match frame:
            case 0:
                # hitbox info here, for example, (220,200)
                jumpable = False # So that the player can jump cancel the animation at a certain point
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 1:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 2:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 3:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 4:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 5:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 6:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 7:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 8:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 10:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 11:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 12:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 13:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 15:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 16:
                player.image = pygame.transform.flip(images[5], reverse, False)
        yield

def attack1(player, reverse):
    images = [pygame.image.load(f"./assets/Samurai/secondattack{i}.png") for i in range(1, 6)]
    images.append(pygame.image.load("./assets/Samurai/attack1.png"))
    images.append(pygame.image.load("./assets/Samurai/idle1.png"))
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for frame in frames:
        match frame:
            case 0:
                # hitbox info here, for example, (220,200)
                jumpable = False # So that the player can jump cancel the animation at a certain point
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 1:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 2:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 3:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 4:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 5:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 6:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 7:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 8:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 10:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 11:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 12:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 13:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 15:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 16:
                player.image = pygame.transform.flip(images[6], reverse, False)
        yield

def attack2(player, reverse):
    images = [pygame.image.load(f"./assets/Samurai/attack{i}.png") for i in range(1, 5)]
    images.append(pygame.image.load("./assets/Samurai/attack1.png"))
    images.append(pygame.image.load("./assets/Samurai/idle1.png"))
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for frame in frames:
        match frame:
            case 0:
                # hitbox info here, for example, (220,200)
                jumpable = False # So that the player can jump cancel the animation at a certain point
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 1:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 2:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 3:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 4:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 5:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 6:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 7:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 8:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 10:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 11:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 12:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 13:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 15:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 16:
                player.image = pygame.transform.flip(images[5], reverse, False)
        yield

def idle(player, reverse):
    images = [pygame.image.load(f"./assets/Samurai/idle{i}.png") for i in range(1, 7)]
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for value in range(0, len(frames)):
        match value:
            case 0:
                # hitbox info here, for example, (220,200)
                jumpable = False # So that the player can jump cancel the animation at a certain point
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 1:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 2:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 3:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 4:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 5:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 6:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 7:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 8:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 10:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 11:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 12:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 13:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 15:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 16:
                player.image = pygame.transform.flip(images[5], reverse, False)
        yield

def walk(player, reverse):
    images = [pygame.image.load(f"./assets/Samurai/run{i}.png") for i in range(1, 7)]
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for value in range(0, len(frames)):
        match value:
            case 0:
                jumpable = False
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 1:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 2:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 3:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 4:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 5:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 6:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 7:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 8:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 10:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 11:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 12:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 13:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 15:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 16:
                player.image = pygame.transform.flip(images[5], reverse, False)
        yield

def death(player, reverse):
    images = [pygame.image.load(f"./assets/Samurai/death{i}.png") for i in range(1, 7)]
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for value in range(0, len(frames)):
        match value:
            case 0:
                # hitbox info here, for example, (220,200)
                jumpable = False # So that the player can jump cancel the animation at a certain point
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 1:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 2:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 3:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 4:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 5:
                player.image = pygame.transform.flip(images[1], reverse, False)
                value -= 4
            case 6:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 7:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 8:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 10:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 11:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 12:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 13:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 15:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 16:
                player.image = pygame.transform.flip(images[5], reverse, False)
        yield


def walkBack(player, reverse):
    images = [pygame.image.load(f"./assets/Samurai/run{i}.png") for i in range(1, 7)]
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for value in range(0, len(frames)):
        match value:
            case 0:
                # hitbox info here, for example, (220,200)
                jumpable = False # So that the player can jump cancel the animation at a certain point
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 1:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 2:
                player.image = pygame.transform.flip(images[0], reverse, False)
            case 3:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 4:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 5:
                player.image = pygame.transform.flip(images[1], reverse, False)
            case 6:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 7:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 8:
                player.image = pygame.transform.flip(images[2], reverse, False)
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 10:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 11:
                player.image = pygame.transform.flip(images[3], reverse, False)
            case 12:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 13:
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                player.image = pygame.transform.flip(images[4], reverse, False)
            case 15:
                player.image = pygame.transform.flip(images[5], reverse, False)
            case 16:
                player.image = pygame.transform.flip(images[5], reverse, False)
        yield

# def animationHandler():
#     pygame.init()
#     clock = pygame.time.Clock()
#     attack = None
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_j:
#                     attack = attack1(settings.maxWidth/2, settings.maxHeight/2)
#                 elif event.key == pygame.K_k:
#                     attack = attack2()
#         if attack:
#             try:
#                 next(attack)
#             except StopIteration:
#                 attack = None

#         clock.tick(60)
#         pygame.display.update()
#         pygame.display.flip()
