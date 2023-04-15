from typing import List, Tuple

class Arena:
    def __init__(self, space: List[List[str]]):
        self.space = space
        self.robotPosition = self.get_robot_position()

    def has_sticker(self, x: int, y: int) -> bool:
        return self.space[x][y] == "*"

    def has_pillar(self, x: int, y: int) -> bool:
        return self.space[x][y] == "#"

    def get_robot_position(self) -> Tuple[str, Tuple[int, int]]:
        for x, row in enumerate(self.space):
            for y, cell in enumerate(row):
                if cell in ["N", "L", "S", "O"]:
                    orientation = cell
                    robot_position = (x, y)
                    return (orientation, robot_position)

    @staticmethod
    def construct_arena(rows_quantity: int) -> 'Arena':
        space_to_build = []
        for _ in range(rows_quantity):
            row = list(input())
            space_to_build.append(row)
        return Arena(space_to_build)

class Robot:
    def __init__(self, arena: 'Arena'):
        self.arena = arena

    def move(self) -> bool:
        orientation, (x, y) = self.arena.robotPosition
        if orientation == "N":
            new_x = x - 1
            new_y = y
        elif orientation == "L":
            new_x = x
            new_y = y + 1
        elif orientation == "S":
            new_x = x + 1
            new_y = y
        else:
            new_x = x
            new_y = y - 1
        if new_x < 0 or new_x >= len(self.arena.space) or new_y < 0 or new_y >= len(self.arena.space[0]):
            return False
        has_pillar_in_new_cell = self.arena.has_pillar(new_x, new_y)
        if has_pillar_in_new_cell:
            return False
        has_sticker_in_new_cell = self.arena.has_sticker(new_x, new_y)
        self.arena.space[x][y] = "."
        self.arena.space[new_x][new_y] = orientation
        self.arena.robotPosition = (orientation, (new_x, new_y))
        return has_sticker_in_new_cell

    def turn(self, direction: str):
        orientation, (x, y) = self.arena.robotPosition
        orientations = ["N", "L", "S", "O"]
        current_orientation = orientations.index(orientation)
        if direction == "right":
            new_orientation = orientations[(current_orientation + 1) % 4]
        else:
            new_orientation = orientations[(current_orientation - 1) % 4]
        self.arena.robotPosition = (new_orientation, (x, y))
        self.arena.space[x][y] = new_orientation

class Game:
    def __init__(self, arena: 'Arena', robot: 'Robot', score: int = 0):
        self.arena = arena
        self.robot = robot
        self.score = score

    def get_robot_instructions(self) -> List[str]:
        return list(input())

    def execute_instruction(self, instruction: str):
        if instruction == "F":
            has_sticker = self.robot.move()
            if has_sticker:
                self.score += 1
        elif instruction == "D":
            self.robot.turn("right")
        elif instruction == "E":
            self.robot.turn("left")

    def finish_game(self):
        return self.score
    
while True:
    arena_rows, _, _ = [int(x) for x in input().split()]
    if arena_rows == 0:
        break
    arena = Arena.construct_arena(arena_rows)
    robot = Robot(arena)
    game = Game(arena, robot)
    robot_instructions = game.get_robot_instructions()
    for instruction in robot_instructions:
        game.execute_instruction(instruction)
    print(game.finish_game())
