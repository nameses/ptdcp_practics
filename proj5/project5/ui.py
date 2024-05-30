import tkinter as tk
from tkinter import filedialog, Canvas, messagebox
from ui2 import show_draw_window
from main import QAlgorithm

def upload_file():
    file_path = filedialog.askopenfilename(
        initialdir="./",
        title="Select a File",
        filetypes=(("Text files", "*.txt*"), ("all files", "*.*"))
    )

    if file_path:
        process_file(file_path)


def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            matrix = [list(map(int, line.strip())) for line in file]
            handle(matrix)
    except Exception as e:
        print(f"Error reading file: {e}")


def validate_and_trim_map(matrix):
    start_points = 0
    finish_points = 0

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Validate the map
    for row in matrix:
        start_points += row.count(2)
        finish_points += row.count(3)

    if start_points != 1:
        raise ValueError(f"Invalid map: expected exactly one start point, found {start_points}.")

    if finish_points != 1:
        raise ValueError(f"Invalid map: expected exactly one finish point, found {finish_points}.")

    # Find the bounding box of the non-empty area
    min_row, max_row = rows, -1
    min_col, max_col = cols, -1

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 0:
                if r < min_row:
                    min_row = r
                if r > max_row:
                    max_row = r
                if c < min_col:
                    min_col = c
                if c > max_col:
                    max_col = c

    # Extract the trimmed matrix
    trimmed_matrix = []
    for r in range(min_row, max_row + 1):
        trimmed_matrix.append(matrix[r][min_col:max_col + 1])

    return trimmed_matrix


def show_results(matrix):
    canvas.delete("all")  # Clear the canvas before drawing
    cell_size = 20  # Size of each cell
    colors = {0: "white", 1: "black", 2: "red", 3: "green", 4: "blue"}

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=colors.get(value, "white"))

def handle(input_matrix):
    try:
        input_matrix = validate_and_trim_map(input_matrix)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return
    q = QAlgorithm()
    show_results(q.get_output_matrix(input_matrix)) #instead of input matrix, put the output matrix here

# Create the main application window
root = tk.Tk()
root.title("Find a way from labyrinth")
root.geometry("600x600")
def show_draw():
    show_draw_window(tk.Toplevel(root), handle)

# Create and place a button to upload a file
tk.Button(root, text="Upload File", command=upload_file).pack(pady=20)
tk.Button(root, text="Draw Labyrinth", command=show_draw).pack(pady=20)
# Create a canvas to draw the matrix
canvas = Canvas(root, width=500, height=500, bg="white")
canvas.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
