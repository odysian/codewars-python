# https://www.codewars.com/kata/58663693b359c4a6560001d6/train/python


def maze_runner(maze, directions):

    # Find starting point with nested loop
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                coords = [i, j]
                break

    # Make move, apply move to coords and use them as inputs
    for move in directions:
        if move == "N":
            coords[0] -= 1
        elif move == "S":
            coords[0] += 1
        elif move == "E":
            coords[1] += 1
        elif move == "W":
            coords[1] -= 1

        # Out of bounds check
        # Check before accessing maze to prevent IndexError
        # len(maze) is out of bounds because of zero index
        if (
            coords[0] < 0
            or coords[0] >= len(maze)
            or coords[1] < 0
            or coords[1] >= len(maze[0])
        ):
            return "Dead"

        # Check position
        pos = maze[coords[0]][coords[1]]
        if pos == 3:
            return "Finish"
        if pos == 1:
            return "Dead"

    return "Lost"
