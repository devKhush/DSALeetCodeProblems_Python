from typing import List, Tuple


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]) -> None:
        self.width = width
        self.height = height
        self.food = food
        self.score = 0
        self.snakeBody = [(0,0)]

    def move(self, direction: str) -> int:
        head_row, head_column = self.snakeBody[-1]

        if direction == 'U':
            head_row -= 1
        elif direction == 'D':
            head_row += 1
        elif direction == 'L':
            head_column -= 1
        elif direction == 'R':
            head_column += 1

        if head_row < 0 or head_row >= self.height or head_column < 0 or head_column >= self.width:
            return -1

        if self.food and [head_row, head_column] == self.food[0]:
            self.score += 1
            self.snakeBody.append([head_row, head_column])
            self.food.pop(0)
        else:
            self.snakeBody.pop(0)
            if [head_row, head_column] in self.snakeBody:
                return -1
            else:
                self.snakeBody.append([head_row, head_column])

        return self.score


width_ = 3
height_ = 2
food_ = [[1, 2], [0, 1]]

snakeGame = SnakeGame(width=width_, height=height_, food=food_)

print(snakeGame.move('R'))
print(snakeGame.move('D'))
print(snakeGame.move('R'))
print(snakeGame.move('U'))
print(snakeGame.move('L'))
print(snakeGame.food)
print(snakeGame.move('U'))
