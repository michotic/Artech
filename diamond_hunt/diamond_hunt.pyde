points = []
gems = []
gem_amount = 10
player_speed = 10
time_limit = 60 * 10
object_size = 64

def setup():
    # Configure canvas/game window
    size(640, 480)
    noSmooth()
    imageMode(CENTER)
    textSize(20)
    # Load in sprites/artwork
    global player_img, gem_img, background_img
    player_img = loadImage("miner.png")
    gem_img = loadImage("gem.png")
    background_img = loadImage("background.png")
    
    global player
    player = PVector(width / 2, height / 2)
    
    for i in range(gem_amount):
        gem_x = random(width * 0.1, width * 0.9)
        gem_y = random(height * 0.1, height * 0.9)
        gems.append(PVector(gem_x, gem_y))
    

def draw():
    # Draw background & player
    image(background_img, width / 2, height / 2, width, height)
    image(player_img, player.x, player.y, object_size, object_size)
    
    # Render gems
    for gem in gems:
        image(gem_img, gem.x, gem.y, object_size, object_size)
        # Gem collision check
        if dist(player.x, player.y, gem.x, gem.y) < object_size:
            points.append(1)
            gem.x = width * 2
            
        
    # Write score and time remaining on canvas
    text('Points: ' + str(len(points)), 30, 30)
    text('Time Left: ' + str(time_limit - frameCount), 30, 50)
    
    # WIN CONDITIONS
    if (time_limit - frameCount <= 0):
        textAlign(CENTER)
        if len(points) == gem_amount:
            text('YOU WIN', width / 2, height / 2)
        else:
            text('YOU LOSE', width / 2, height / 2)
        noLoop()

# MOVEMENT CODE
def keyTyped():
    if key == 'w':
        player.y -= player_speed
    if key == 'a':
        player.x -= player_speed
    if key == 's':
        player.y += player_speed
    if key == 'd':
        player.x += player_speed
        
