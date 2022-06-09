
def setup():
    # Create a canvas with a size of (width, height)
    size(1280, 720)
    # Use our createSprites() function
    createSprites()
    # Turn off smoothening (so our pixel art doesn't become blurry)
    noSmooth()
    # How many pixels long tiles will be 
    global block_size, blocks
    block_size = 32
    blocks = []
    
    generateWorld()
    
    global player
    player = Player(width / 2, 0)
    
    global gravity
    gravity = 3
    
    global hotbar
    hotbar = Hotbar(20, 30)
    
    

def draw():
    # Makes the background blue (R, G, B)
    background(0, 200, 255)
    
    # For all objects in blocks, use their render function
    for block in blocks:
        block.render()
        
    player.render()
    hotbar.render()
        

# Creates sprites out of our spritesheet
def createSprites():
    global spritesheet, sprites
    # loads in spritesheet image
    spritesheet = loadImage("spritesheet.png")
    # size of sprites in the sprite sheet file (16 pixels in this case)
    img_size = 16 
    # sprites will contain all the images we use in our game, we'll access them with the block type 
    sprites = {}
    # here we get the section of the spritesheet we want (x, y, width, height) and add it to sprites  
    sprites["grass"] = spritesheet.get(img_size * 1, img_size * 0, img_size, img_size)
    sprites["dirt"] = spritesheet.get(img_size * 2, img_size * 0, img_size, img_size)
    sprites["wood"] = spritesheet.get(img_size * 3, img_size * 0, img_size, img_size)
    sprites["leaf"] = spritesheet.get(img_size * 4, img_size * 0, img_size, img_size)
    sprites["rock"] = spritesheet.get(img_size * 2, img_size * 1, img_size, img_size)
    sprites["coal"] = spritesheet.get(img_size * 3, img_size * 1, img_size, img_size)
    sprites["flower1"] = spritesheet.get(img_size * 1, img_size * 1, img_size, img_size)
    sprites["flower2"] = spritesheet.get(img_size * 1, img_size * 2, img_size, img_size)
    sprites["brick"] = spritesheet.get(img_size * 4, img_size * 1, img_size, img_size)
    sprites["player"] = spritesheet.get(img_size * 2, img_size * 2, img_size, img_size)
    sprites["plank"] = spritesheet.get(img_size * 3, img_size * 2, img_size, img_size)
    
    global breaking
    breaking = {}
    breaking[4] = spritesheet.get(img_size * 0, img_size * 3, img_size, img_size)
    breaking[3] = spritesheet.get(img_size * 0, img_size * 2, img_size, img_size)
    breaking[2] = spritesheet.get(img_size * 0, img_size * 1, img_size, img_size)
    breaking[1] = spritesheet.get(img_size * 0, img_size * 0, img_size, img_size)

# Called whenever the mouse is clicked
def mousePressed():
    if mouseButton == RIGHT:
        occupied = False
        for block in blocks:
            if (block.isTouchingMouse()):
                occupied = True
                break
        # Creates a block at the mouse position and adds it to blocks
        blockX = mouseX / block_size
        blockY = mouseY / block_size
        if (occupied == False):
            blocks.append(Block(blockX, blockY, hotbar.getSelected()))
        
    elif mouseButton == LEFT:
        # if left click, look through blocks to see if one was touching the mouse
        for block in blocks:
            if (block.isTouchingMouse()):
                block.durability -= 1
                break

def generateWorld():
    world_width = int(width / block_size) + 1
    world_top = 3
    world_bottom = (height / block_size) + 1
    roughness = random(0.01, 0.1)
    
    for x in range(0, world_width, 1):
        surface_y = noise(x * roughness)
        surface_y = int(map(surface_y, 0, 1, world_top, world_bottom))
        for y in range(surface_y, world_bottom, 1):
            # Determine block type
            if y == surface_y:
                # If it's the surface (top of world at this x), make it grass
                block_type = "grass"
            elif y - surface_y < 5:
                # If it's within 5 blocks of the surface, dirt
                block_type = "dirt"
            else:
                # Anything lower is rock with a 5% chance of being coal
                if random(1) < 0.05:
                    block_type = "coal"
                else:
                    block_type = "rock"
            # Add block to world
            blocks.append(Block(x, y, block_type))
            
            
            # If the newest block is grass
            if block_type == "grass":
                # Chance of spawning trees
                if random(1) < 0.15:
                    createTree(x, y-1)
                # Chance of spawning flowers
                if random(1) < 0.5:
                    if random(1) < 0.5:
                        blocks.append(Block(x, y-1, "flower1"))
                    else:
                        blocks.append(Block(x, y-1, "flower2"))
            
def createTree(x, y):
    for logY in range(6):
        new_block = Block(x, y - logY, "wood")
        blocks.append(new_block)
        
    for leafY in range(4, 9):
        for leafX in range(-2, 3):
            new_block = Block(x+leafX, y - leafY, "leaf")
            blocks.append(new_block)

def keyTyped():
    if key == 'a':
        player.position.x -= player.speed.x
    if key == 'd':
        player.position.x += player.speed.x
    if key == 'w':
        player.jump()

# Block class
class Block:
    # Constructor
    def __init__(self, x, y, type):
        self.position = PVector(x, y)
        self.sprite = sprites[type]
        self.render_pos = PVector(self.position.x * block_size, self.position.y * block_size)
        self.durability = 4
        self.healing_frames = 90
        self.healing_timer = self.healing_frames
        decorationals = ["flower1", "flower2", "leaf", "wood"]
        if (type in decorationals):
            self.decorational = True
        else:
            self.decorational = False
    
    # Render function
    def render(self):
        # if durability > 0 (block is not broken)
        if self.durability > 0:
            # show block sprite
            image(self.sprite, self.render_pos.x, self.render_pos.y, block_size, block_size)
            # show current durability sprite
            image(breaking[self.durability], self.render_pos.x, self.render_pos.y, block_size, block_size)
            # if the block is damaged (durability < 4)
            if self.durability < 4:
                # decrease the healing timer
                self.healing_timer -= 1
                # if healing timer reaches 0
                if self.healing_timer <= 0:
                    # increase durability
                    self.durability += 1
                    # reset timer
                    self.healing_timer = self.healing_frames
        else:
            # if blocksdurability is less than 0, it shouldn't exist, so remove it from blocks
            blocks.remove(self)
        
    def isTouchingMouse(self):
        # if mouse XY is within edges of block (relative to top left corner) return true, if not return false
        if mouseX >= self.render_pos.x:
            if mouseX <= self.render_pos.x + block_size:
                if mouseY >= self.render_pos.y:
                    if mouseY <= self.render_pos.y + block_size:
                        return True
        return False
    
class Player:
    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.sprite = sprites["player"]
        self.speed = PVector(5, 0)
        self.block_below = False
        
        self.jumping = False
        self.targetY = 0
        
    def render(self):
        
        self.collisionCheck()
        
        if self.block_below == False and self.jumping == False:
            self.speed.y = gravity
        elif self.jumping == True and self.position.y <= self.targetY:
            self.jumping = False
        elif self.block_below == True and self.jumping == False:
            self.speed.y = 0
        
        self.position.y += self.speed.y
        
        image(self.sprite, self.position.x, self.position.y, block_size, block_size)
        
    def jump(self):
        if (self.jumping == False) and (self.block_below == True):
            self.jumping = True
            self.speed.y = -gravity
            self.targetY = self.position.y - block_size * 2.5
        
    def collisionCheck(self):
        self.block_below = False
        for block in blocks:
            if block.decorational == False:
                if abs(self.position.x - block.render_pos.x) < block_size * 0.8:
                    if self.position.y >= block.render_pos.y - block_size:
                        if self.position.y < block.render_pos.y:
                            self.block_below = True
                            self.position.y = block.render_pos.y - block_size
                            
                if abs(self.position.y - block.render_pos.y) < block_size * 0.9:
                    if self.position.x + block_size > block.render_pos.x:
                        if self.position.x < block.render_pos.x:
                            self.position.x = block.render_pos.x - block_size
                            
                    if self.position.x - block_size <= block.render_pos.x:
                        if self.position.x > block.render_pos.x:
                            self.position.x = block.render_pos.x + block_size
                            
class Hotbar:
    def __init__(self, x, y):
        self.position = PVector(x, y)
        
        self.icons = ["brick", "coal", "rock", "wood", "plank", "leaf", "grass", "dirt", "flower1", "flower2"]
        self.icon_size = block_size * 0.8
        self.selected = 0
        
    def render(self):
        for icon in range(len(self.icons)):
            renderX = self.position.x + (block_size * icon)
            renderY = self.position.y
            
            if mousePressed:
                if self.isTouchingMouse(renderX, renderY):
                    self.selected = icon
            
            fill(30)
            if icon == self.selected:
                fill(255)
            noStroke()
            rect(renderX- block_size*0.1, renderY- block_size*0.1, block_size, block_size)
            image(sprites[self.icons[icon]], renderX, renderY, self.icon_size, self.icon_size)
            
    def isTouchingMouse(self, x, y):
        # if mouse XY is within edges of block (relative to top left corner) return true, if not return false
        if mouseX >= x:
            if mouseX <= x + block_size:
                if mouseY >= y:
                    if mouseY <= y + block_size:
                        return True
                    
    def getSelected(self):
        return self.icons[self.selected]
            
                            
                        
