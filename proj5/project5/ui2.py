import tkinter as tk
from tkinter import Canvas, Button, Radiobutton, StringVar

def show_draw_window(root, handle):

    def draw_matrix_on_canvas(event):

        x, y = event.x, event.y
        row, col = y // cell_size, x // cell_size

        if 0 <= row < rows and 0 <= col < cols:
            canvas.itemconfig(rectangles[row][col], fill=current_color)
            matrix[row][col] = color_mapping[current_color]


    def save_matrix():
        nonlocal handle
        root.destroy()
        handle(matrix)
        # print("Current matrix:")
        # for row in matrix:
        #     print(row)


    # Parameters
    cell_size = 20
    rows, cols = 25, 25

    # Colors
    colors = ["white", "black", "red", "green"]
    color_mapping = {"white": 0, "black": 1, "red": 2, "green": 3}
    color_name_mapping = {"white": "Empty cell", "black": "Barrier", "red": "Start", "green": "Final"}
    current_color = "white"

    def select_color():
        nonlocal current_color
        current_color = color_var.get()
    # Initialize matrix
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Create the main application window
    root.title("Draw Matrix")
    root.geometry(f"{cols * cell_size + 20}x{rows * cell_size + 100}")

    # Create a canvas to draw the matrix
    canvas = Canvas(root, width=cols * cell_size, height=rows * cell_size, bg="white")
    canvas.pack(pady=20)

    # Create rectangles on the canvas
    rectangles = [[None for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            rectangles[i][j] = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray")

    # Bind mouse events to canvas
    canvas.bind("<B1-Motion>", draw_matrix_on_canvas)
    canvas.bind("<Button-1>", draw_matrix_on_canvas)

    # Add color selection radio buttons
    color_var = StringVar(value="white")
    for color in colors:
        Radiobutton(root, text=color_name_mapping[color], variable=color_var, value=color, command=select_color).pack(side="left",
                                                                                                               padx=10)

    # Add button to save matrix
    save_button = Button(root, text="Save Matrix", command=save_matrix)
    save_button.pack(pady=10)


