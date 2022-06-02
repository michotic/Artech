moles = []
whacked_moles = []

def setup():
    size(500, 500)
    noSmooth()
    imageMode(CENTER)
    
    global mole_size, mole_img, mole_count
    mole_size = 64
    mole_img = loadImage("mole.png")
    mole_count = 32
    for i in range(mole_count):
        mole_x = random(width)
        mole_y = random(height)
        mole_alive = 1 # 0 = dead, 1 = alive
        moles.append(PVector(mole_x, mole_y, mole_alive))
    
def draw():
    background('#79D80D')
    
    for mole in moles:
        if mole.z == 1:
            image(mole_img, mole.x, mole.y, mole_size, mole_size)
            if random(1) < 0.01:
                mole.x = random(width)
                mole.y = random(height)
                
    textSize(30)
    text('Points: ' + str(len(whacked_moles)), 30, 30)
    
    if (len(whacked_moles) == mole_count):
        push()
        textAlign(CENTER)
        text('YOU WIN!', width / 2, height / 2)
        pop()
                    
def mousePressed():
    for mole in moles:
        if dist(mouseX, mouseY, mole.x, mole.y) < mole_size / 2 and mole.z == 1:
            mole.z = 0
            whacked_moles.append(mole)
