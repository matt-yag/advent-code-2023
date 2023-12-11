import sys
from functools import reduce


def x(list):
    """Returns a sum of all elements in the list"""
    return reduce(lambda x, y: x + y, list)


def o(list):
    """Returns a product of all elements in the list"""
    return reduce(lambda x, y: x * y, list)


def c(*args):
    """Prints element"""
    print(args)


def aoc(sufix=''):
    if len(sys.argv) == 1:
        file_path = 'input.txt'
    else:
        file_path = 'input-test%s.txt' % sufix
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


import matplotlib.pyplot as plt
import numpy as np


class MatrixDrawer:
    def __init__(self, matrix):
        self.matrix = matrix
        self.cell_size = 45
        self.line_thickness = 1
        self.grid_color = (0.9, 0.9, 0.9)  # Light gray color for the grid lines
        self.img_width = self.cell_size * len(matrix[0])
        self.img_height = self.cell_size * len(matrix)


    def draw_grid(self, ax):
        # Draw the grid lines and indices
        for i in range(len(self.matrix[0]) + 1):
            ax.axvline(i * self.cell_size, color=self.grid_color, linewidth=1)
        for i in range(len(self.matrix) + 1):
            ax.axhline(i * self.cell_size, color=self.grid_color, linewidth=1)
            for j in range(len(self.matrix[0])):
                #pass
                if i < len(self.matrix):
                    ax.text(j * self.cell_size + 5, i * self.cell_size + 15, f'({i},{j})', color='grey', fontsize=8)

    def draw_matrix(self, ax):
        # Draw lines based on the matrix values
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                center_x = x * self.cell_size + self.cell_size // 2
                center_y = y * self.cell_size + self.cell_size // 2
                if self.matrix[y][x] == '-':
                    ax.plot([x * self.cell_size, x * self.cell_size + self.cell_size], [center_y, center_y], 'k-',
                            lw=self.line_thickness)
                elif self.matrix[y][x] == '|':
                    ax.plot([center_x, center_x], [y * self.cell_size, y * self.cell_size + self.cell_size], 'k-',
                            lw=self.line_thickness)
                elif self.matrix[y][x] == 'F':
                    ax.plot([center_x, center_x], [y * self.cell_size + self.cell_size, center_y], 'k-',
                            lw=self.line_thickness)
                    ax.plot([center_x, x * self.cell_size + self.cell_size], [center_y, center_y], 'k-',
                            lw=self.line_thickness)
                elif self.matrix[y][x] == '7':
                    ax.plot([center_x, center_x], [y * self.cell_size + self.cell_size, center_y], 'k-',
                            lw=self.line_thickness)
                    ax.plot([center_x, x * self.cell_size], [center_y, center_y], 'k-', lw=self.line_thickness)
                elif self.matrix[y][x] == 'J':
                    ax.plot([center_x, center_x], [y * self.cell_size, center_y], 'k-', lw=self.line_thickness)
                    ax.plot([center_x, x * self.cell_size], [center_y, center_y], 'k-', lw=self.line_thickness)
                elif self.matrix[y][x] == 'L':
                    ax.plot([center_x, center_x], [y * self.cell_size, center_y], 'k-', lw=self.line_thickness)
                    ax.plot([center_x, x * self.cell_size + self.cell_size], [center_y, center_y], 'k-',
                            lw=self.line_thickness)

    def draw_line_between_cells(self, ax, y1, x1, y2, x2, direction_to, direction_from):

        if y1 == y2:
            start_x = x1 * self.cell_size + (
                self.cell_size // 3 if 'L' in direction_to else self.cell_size * 2 // 3 if 'R' in direction_to else self.cell_size // 2)
            end_x = x2 * self.cell_size + (
                self.cell_size // 3 if 'L' in direction_from else self.cell_size * 2 // 3 if 'R' in direction_from else self.cell_size // 2)
            start_y = y1 * self.cell_size + (
                self.cell_size // 3 if 'T' in direction_to else self.cell_size * 2 // 3 if 'B' in direction_to else self.cell_size // 2)
            end_y = start_y

            if ('T' not in direction_from and 'T' in direction_to) or ('B' not in direction_from and 'B' in direction_to):
                sx = x2 * self.cell_size + (
                    self.cell_size // 3 if 'L' in direction_from else self.cell_size * 2 // 3 if 'R' in direction_from else self.cell_size // 2)
                ex = sx
                sy = y2 * self.cell_size + (
                    self.cell_size // 3 if 'T' in direction_to else self.cell_size * 2 // 3 if 'B' in direction_to else self.cell_size // 2)
                ey = y2 * self.cell_size + (
                    self.cell_size // 3 if 'T' in direction_from else self.cell_size * 2 // 3 if 'B' in direction_from else self.cell_size // 2)
                ax.plot([sx, ex], [sy, ey], 'r-', lw=self.line_thickness / 3)

        elif x1 == x2:
            start_x = x1 * self.cell_size + (
                self.cell_size // 3 if 'L' in direction_to else self.cell_size * 2 // 3 if 'R' in direction_to else self.cell_size // 2)
            end_x = start_x
            start_y = y1 * self.cell_size + (
                self.cell_size // 3 if 'T' in direction_to else self.cell_size * 2 // 3 if 'B' in direction_to else self.cell_size // 2)
            end_y = y2 * self.cell_size + (
                self.cell_size // 3 if 'T' in direction_from else self.cell_size * 2 // 3 if 'B' in direction_from else self.cell_size // 2)

            if ('L' not in direction_from and 'L' in direction_to) or ('R' not in direction_from and 'R' in direction_to):
                sx = x2 * self.cell_size + (
                    self.cell_size // 3 if 'L' in direction_to else self.cell_size * 2 // 3 if 'R' in direction_to else self.cell_size // 2)
                ex = x2 * self.cell_size + (
                    self.cell_size // 3 if 'L' in direction_from else self.cell_size * 2 // 3 if 'R' in direction_from else self.cell_size // 2)
                sy = y2 * self.cell_size + (
                    self.cell_size // 3 if 'T' in direction_from else self.cell_size * 2 // 3 if 'B' in direction_from else self.cell_size // 2)
                ey = sy
                ax.plot([sx, ex], [sy, ey], 'r-', lw=self.line_thickness / 3)

        # Draw the line
        ax.plot([start_x, end_x], [start_y, end_y], 'r-', lw=self.line_thickness / 3)

    def show(self, dpi=300):
        self.dpi = dpi
        inches_per_px = 1.0 / dpi  # Inches per pixel
        fig_width = self.img_width * inches_per_px # Width in inches
        fig_height = self.img_height * inches_per_px # Height in inches

        # Create a figure with the calculated size
        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        ax.set_xlim([0, self.img_width])
        ax.set_ylim([self.img_height, 0])
        ax.axis('off')  # Hide the axis

        # Draw the grid, matrix, and any lines between cells
        self.draw_grid(ax)
        self.draw_matrix(ax)

        self.fig = fig

        return ax


    def save(self, filename='matrix_plot.png'):
        # Display the image
        self.fig.savefig(filename, dpi=self.dpi, bbox_inches='tight')
