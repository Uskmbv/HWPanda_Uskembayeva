def print_labyrinth(lab: list[str]):
    for row in lab:
        print(row)


labyrinth = [

    "███████",
    "█     █",
    "█   ███",
    "█ ███ █",
    "█     █",
    "███████",

]

print_labyrinth(labyrinth)


# phase two

def prompt_integer(message: str) -> int:
    user_input = input(message)  # Ask the user for input
    return int(user_input)  # Convert the input to an integer and return it


def prompt_user_for_location(name: str) -> tuple[int, int]:
    print(f"Enter the {name} location:")
    row = prompt_integer("Row: ")  # Ask for the row
    column = prompt_integer("Column: ")  # Ask for the column
    return row, column  # Return the row and column as a tuple


# Get the start location
start = prompt_user_for_location("start")

# Get the end location
end = prompt_user_for_location("end")

# Accessing the row and column of start location using indices
start_row = start[0]
start_column = start[1]

# Accessing the row and column of end location using tuple unpacking
end_row, end_column = end

# phase three

from collections import deque

def is_valid_move(lab, visited, row, col):
    rows = len(lab)
    cols = len(lab[0])
    return 0 <= row < rows and 0 <= col < cols and lab[row][col] == ' ' and not visited[row][col]

def bfs(lab, start, end):
    rows = len(lab)
    cols = len(lab[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start, [start])])

    while queue:
        (row, col), path = queue.popleft()
        visited[row][col] = True

        if (row, col) == end:
            return path

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(lab, visited, new_row, new_col):
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
                visited[new_row][new_col] = True

    return []


start = (3, 5)
end = (1, 3)
path = bfs(labyrinth, start, end)
print(path)

def print_labyrinth_with_path(lab, path):
    rows = len(lab)
    cols = len(lab[0])

    # Create a copy of the labyrinth to avoid modifying the original
    labyrinth_copy = [list(row) for row in lab]

    # Mark the path with 'X'
    for row, col in path:
        labyrinth_copy[row][col] = 'X'

    # Print the labyrinth with the path
    print("".join(str(i % 10) for i in range(cols)))
    for row in labyrinth_copy:
        print("".join(row))

# Example usage
labyrinth = [
    "███████",
    "█     █",
    "█   ███",
    "█ ███ █",
    "█     █",
    "███████"
]

start = (3, 5)
end = (1, 3)
path = [(3, 5), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (1, 3)]

print_labyrinth_with_path(labyrinth, path)


