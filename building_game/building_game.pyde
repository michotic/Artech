'''
2D Tile Based World Demo

Made for Artech Camps
'''
tile_size = 32 # The length of each side of a tile in our world (in pixels)
tiles = [] # The list that will hold all the tiles
        

def setup():
    size(640, 480)
    noSmooth()
    global brick_img
    brick_img = loadImage("brick.png")
    
def draw():
    background(50, 160, 240)
    for tile_obj in tiles:
        fill(255)
        #rect(tile_obj.x, tile_obj.y, tile_size, tile_size)
        image(brick_img, tile_obj.x, tile_obj.y, tile_size, tile_size)
        
    # Draws a rectangle highlighting where the mouse is on the grid
    grid_position = snapToGrid(mouseX, mouseY)
    fill(255, 255, 255, 30)
    rect(grid_position.x, grid_position.y, tile_size, tile_size)

def mouseDragged():
    grid_position = snapToGrid(mouseX, mouseY)
    #grid_position = PVector(mouseX, mouseY)
    tiles.append(grid_position)

def snapToGrid(x, y):
    grid_x = int(x / tile_size) * tile_size
    grid_y = int(y / tile_size) * tile_size
    grid_position = PVector(grid_x, grid_y)
    return grid_position
