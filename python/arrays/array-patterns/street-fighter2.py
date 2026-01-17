# https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python


def street_fighter_selection(fighters, initial_position, moves):
    # Map positions to row by col
    row, col = initial_position
    result = []
    for move in moves:
        # Up and down a bit confusing because row 1 is below row 0
        if move == "up":
            # If at top, stay there, if at bottom, move up
            row = max(0, row - 1)
        elif move == "down":
            # If at bottom, stay there, if at top move down
            row = min(1, row + 1)
        elif move == "left":
            # Wraps around, works with negative values as well
            col = (col - 1) % 6
        elif move == "right":
            col = (col + 1) % 6
        result.append(fighters[row][col])
    return result
