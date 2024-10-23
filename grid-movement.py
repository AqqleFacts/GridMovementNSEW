grid = [
    [2, 1, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
]

piece = [0, 0]

def direction_action(letter):
    posX = piece[0]
    posY = piece[1]
    if letter == 'e' and grid[posX][posY+1] != 0:
        piece[1] += 1
        grid[posX][posY] = 1
        grid[posX][posY+1] = 2
    elif letter == 'w' and grid[posX][posY-1] != 0:
        piece[1] -= 1
        grid[posX][posY] = 1
        grid[posX][posY-1] = 2
    elif letter == 's' and grid[posX+1][posY] != 0:
        piece[0] += 1
        grid[posX][posY] = 1
        grid[posX+1][posY] = 2
    elif letter == 'n' and grid[posX-1][posY] != 0:
        piece[0] -= 1
        grid[posX][posY] = 1
        grid[posX-1][posY] = 2
    else:
        print('INVALID DIRECTION')

def show(room):
    for row in room:
        for cell in row:
            if cell == 0:
                print('|', end=' ')
            elif cell == 1:
                print('-', end=' ')
            elif cell == 2:
                print('x', end=' ')
        print()

def run():
    while True:
        show(grid)
        movement = input("N S E W").lower() 
        if movement in ['n', 'e', 's', 'w']:
            direction_action(movement)
            print()
            break 
        else:
            print("Invalid: N S E W:")

while True:
    run()    