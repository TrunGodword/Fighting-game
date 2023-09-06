import pygame, settings

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, up, down, left, right, color, health, attackA, sizex, sizey, top):
        super().__init__()
        self.image = pygame.image.load("./assets/Samurai/idle1.png")
        # pygame.Surface((sizex, sizey))
        # self.body = pygame.image.load("./assets/Samurai/air1.png")
        # self.color = (color)
        # self.image.fill((color))
        self.rect = self.image.get_rect(bottomleft = (x, y) )
        self.x = x
        self.y = y
        self.rect.width = 195 - sizex
        self.rect.height = sizey + 70
        self.rect.x = x
        self.rect.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.speed = 10
        self.health = health
        self.jumping = False
        self.animate = None
        self.state = {"idle": False, "jumping": False, "attacking": False}
        self.top = top
        
        self.mass = 20
        self.gravity = 10
        self.initialmass = self.mass
        self.dt = round(1/60, 4)

        
        self.up =  up
        self.down = down
        self.left = left
        self.right = right
        self.attackA = attackA
        self.state["idle"] = True
    
        self.current_health = 1000
        self.target_health = 1000
        self.max_health = 1000
        self.health_bar_length = 400
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 3

    def get_damage(self,amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self,amount):
        if self.target_health < self.max_health:
            self.target_health += amount
             
             
        if self.target_health > self.max_health:
            self.target_health = self.max_health

    def advanced_health(self):
        transition_width = 0
        transition_color = (255,0,0)

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (0,255,0)

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed 
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (255,255,0)

        health_bar = pygame.Rect(10,self.top,int(self.current_health / self.health_ratio),25)
        transition_bar = pygame.Rect(health_bar.left,self.top,transition_width,25)
		
        pygame.draw.rect(settings.screen,(255,0,0),health_bar)
        pygame.draw.rect(settings.screen,transition_color,transition_bar)	
        pygame.draw.rect(settings.screen,(255,255,255),(10,self.top,self.health_bar_length,25),4)	
              
    def update(self):
        self.advanced_health()
        keys = pygame.key.get_pressed()
        
        if self.mass < self.initialmass:
            self.mass += 1
        
        self.rect.y += self.mass + (self.gravity * self.dt)

        if keys[self.left]:
            self.rect.x -= self.speed
        if keys[self.right]:
            self.rect.x += self.speed
            # self.animate = animation.walk(self)
        if keys[self.up] and self.jumping == False:
            self.mass = -self.mass
            self.jumping = True
        # if self.state["idle"]:
        #     self.animate = animation.idle(self)

        # if self.animate:
        #     try:
        #         next(self.animate)
        #     except StopIteration:
        #         self.animate = None



        # Collision for the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > settings.maxWidth:
            self.rect.right = settings.maxWidth
    
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom >= settings.maxHeight:
            self.rect.bottom = settings.maxHeight
            self.jumping = False
