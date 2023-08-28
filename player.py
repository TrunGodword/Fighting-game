import sys, pygame

class Player(pygame.sprite.Sprite):
    # def __init__ буюу Class хуваарьлагдахад автоматаар уншигдах функц:
    # Хамгийн эхний (self) гэж буй нь өөрт хуваарьлагдаж буй бүх өгөгдлийг өөр дээрээ буулгаж өгөх нэршил юм.
    def __init__(self, x, y, up, down, left, right, color, health, attackA):
        super().__init__()
        # Player character-ийн урт ба өргөн.
        self.image = pygame.Surface((50, 70))
        # Player character-ийн өнгө.
        self.color = (color)
        self.image.fill((color))
        # Өнгө ба урт, өргөний хэмжээг өгсөний дараа хэмжээний өгөгдлүүдийг өөр дээрээ self.rect гэж авах
        self.rect = self.image.get_rect()
        # Self.rect-ийн x ба y хэмжээг мөн өөр дээрээ авах.
        self.rect.x = x
        self.rect.y = y
        # Player character-ийн хурд ба амь.
        self.speed = 10
        self.health = health
        self.mass = 20
        self.gravity = 10
        self.jumping = False
        self.jumpcd = 40
        self.initialmass = self.mass
        self.dt = round(1/60, 4)
        
        # up, down, left, right-ийн оронд бид гар keyboard-ний товчлуурууд хуваарьлах бөгөөд self.up/down/left/right дээр тусгаж авч буй нь:
        self.up =  up
        self.down = down
        self.left = left
        self.right = right
        self.attackA = attackA
    
    # Update хэсэг буюу Player character-ийн EVENT LOOP:
    def update(self):
        # Энэ нь Товчлуур дарагдаж буйг шалгадаг функцийг өөр дээрээ хадгалж өгч байгаа юм.
        keys = pygame.key.get_pressed()

        
        if self.mass < self.initialmass:
            self.mass += 1

        if self.jumping == True and self.jumpcd >= 1:
            self.jumpcd -= 1
        else:
            self.jumping = False
            self.jumpcd = 40
                
        
        self.rect.y += self.mass + (self.gravity * self.dt)

        # Дараа нь, left, right, up, down гэдэг дээр хуваарьлагдсан товчнууд дарагдаж байвал 
        # Player character-ийн x эсвэл y өгөгдлийг өөрийнх нь speed өгөгдлөөр хасч эсвэл нэмж өгч буй нь
        if keys[self.left]:
            self.rect.x -= self.speed
        if keys[self.right]:
            self.rect.x += self.speed
        if keys[self.up] and self.jumping == False:
            self.mass = -(self.mass)
            self.jumping = True
    
        
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #     elif event.type == pygame.KEYDOWN:
        #         if event.key == self.up:
        #             self.jumping = True

        # Дэлгэцнээс гардаггүй болох хэсэг.
        # Хэрвээ Player character-ийн x эсвэл y дэлгэцний өөрийн урт эсвэл өргөнөөс хэтэрвэл,
        # эсвэл 0 буюу дэлгэцний хүрээнээс хэтэрвэл x ба y өгөгдлүүдийг тэнд нь тэнцүүлж буюу гацсан мэт еффектийг оруулах.
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 640:
            self.rect.right = 640
    
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480