
import random

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

print(type(UP))

class Snake():
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, position):
        self.body = self.body[1:] + [position]

    def set_direction(self, direction):
        self.direction = direction

    def get_position(self):
        return self.body[-1]
    
    def get_direction(self):
        return self.direction


class Apple():
    def __init__(self, init_location):
        self.location = init_location

    def get_location(self):
        return self.location

class Game():
    def __init__(self, height, width, minApples):
        self.height = height
        self.width = width
        self.snake = Snake([(2, 2), (2, 3), (2, 4), (2, 5)], RIGHT)
        self.apples = []
        self.minApples = minApples
    
    def board_matrix(self):
        board = []
        
        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append(".")
                    
            board.append(row)

        return board

    def move_snake(self, direction):
        self.snake.set_direction(direction)

        snakePos, snakeDir = self.snake.get_position(), self.snake.get_direction()

        stepXPos = snakePos[0] - snakeDir[1]
        stepYPos = snakePos[1] + snakeDir[0]

        if stepYPos < 0:
            stepYPos = self.height - 1
        elif stepYPos >= self.height:
            stepYPos = 0

        if stepXPos < 0:
            stepXPos = self.width - 1
        elif stepXPos >= self.width:
            stepXPos = 0

        stepPosition = (stepXPos, stepYPos)
        
        self.snake.take_step(stepPosition)

    def handle_apples(self):
        if len(self.apples) < self.minApples:
            needed = self.minApples - len(self.apples)
            for i in range(needed):
                rngX = random.randint(0,self.width-1)
                rngY = random.randint(0,self.height-1)
                
                apple = Apple((rngX, rngY))
                self.apples.append(apple)

    def render(self):
        matrix = self.board_matrix()

        for part in self.snake.body:
            matrix[part[0]][part[1]] = "O"

        headPos = self.snake.get_position()
        matrix[headPos[0]][headPos[1]] = "X"

        for apple in self.apples:
            matrix[apple.location[0]][apple.location[1]] = "@"

        for row in matrix:
            print(*row)


## MAIN GAME FUNCTION

WIDTH = 10
HEIGHT = 5
MIN_APPLES = 3

game = Game(WIDTH, HEIGHT, MIN_APPLES)

isRunning = True

while isRunning:
    game.handle_apples()    
    game.render()

    userAction = input("Enter a WASD direction to move in or 'Q to quit: ")
    
    if userAction == 'q':
        isRunning = False
        continue
    elif userAction == 'w':
        game.move_snake(UP)
    elif userAction == 'a':
        game.move_snake(LEFT)
    elif userAction == 's':
        game.move_snake(DOWN)
    elif userAction == 'd':
       game.move_snake(RIGHT)
    else:
        print("\nInvalid command. (W A S D or Q)")
        continue
    
