import tkinter as tk
from tkinter import messagebox

from config import *
import controller
import preferences


class View():

    x_color = X_COLOR
    o_color = O_COLOR
    board_color = BOARD_COLOR

    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.create_game_base()
        self.canvas.bind("<Button-1>", self.on_square_clicked)
        self.xo='XO'
        self.move=0


    def create_game_base(self):
        self.create_top_menu()
        self.create_canvas()
        self.draw_board()
        self.create_bottom_frame()

    def create_top_menu(self):
        self.menu_bar = tk.Menu(self.parent)
        self.create_file_menu()
        self.create_edit_menu()
        self.create_about_menu()

    def create_bottom_frame(self):
        self.bottom_frame = tk.Frame(self.parent, height =64)
        self.info_label = tk.Label(self.bottom_frame, text= "Wins:  Losses: Ties: &  some other stuff down here")
        self.info_label.pack(side='left', padx=8, pady=5)
        self.bottom_frame.pack(fill="x", side="bottom")

    def on_about_menu_clicked(self):
        messagebox.showinfo("Tic-Tac-Toe","Created by:\nRichard Sterling")

    def on_new_game_menu_clicked(self):
        #FIXME don't ask for player names
        self.start_new_game()

    def on_preference_menu_clicked(self):
        self.show_preferences_menu()

    def show_preferences_menu(self):
        preferences.PreferencesWindow(self)
        self.reload_colors(self.x_color, self.o_color, self.board_color)

    def reload_colors(self, xcolor, ocolor, boardcolor):
        self.x_color = xcolor
        self.o_color = ocolor
        self.board_color = boardcolor
        self.draw_board()

    def create_file_menu(self):
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.new_game_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_cascade(label='NewGame', menu=self.new_game_menu)
        self.file_menu.add_command(label="New Game (current configurations)", command=self.on_new_game_menu_clicked)
        self.new_game_menu.add_command(label="Human vs. Human", command=self.on_human_human_clicked)
        self.new_game_menu.add_command(label='Human vs. AI', command=self.on_human_ai_clicked)
        self.parent.config(menu=self.menu_bar)

    def on_human_human_clicked(self):
        pass

    def on_human_ai_clicked(self):
        pass

    def create_edit_menu(self):
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Preferences", command=self.on_preference_menu_clicked)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.parent.config(menu=self.menu_bar)

    def create_about_menu(self):
        self.about_menu = tk.Menu(self.menu_bar,tearoff=0)
        self.about_menu.add_command(label="About", command=self.on_about_menu_clicked)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)
        self.parent.config(menu=self.menu_bar)

    def create_canvas(self):
        canvas_width = NUMBER_OF_COL * DIMENSION_OF_EACH_SQUARE
        canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE
        self.canvas = tk.Canvas(self.parent, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)

    def draw_board(self):
        for row in range(NUMBER_OF_ROWS):
            for col in range(NUMBER_OF_COL):
                x1, y1 = self.get_x_y_coordinate(row, col)
                x2, y2 = x1+DIMENSION_OF_EACH_SQUARE, y1 + DIMENSION_OF_EACH_SQUARE
                self.canvas.create_rectangle(x1,y1,x2,y2, width= 3, fill = self.board_color)

    def on_square_clicked(self, event):
        clicked_row, clicked_column = self.get_clicked_row_column(event)
        #print("Hey you clicked on", clicked_row, clicked_column)
        #FIXME this is not actual,just to see if draw worked
        self.draw_xs_os(event,self.xo[self.move%2])
        self.move+=1

    def get_clicked_row_column(self, event):
        col_size=row_size=DIMENSION_OF_EACH_SQUARE
        clicked_column = event.x // col_size
        clicked_row = 2-(event.y//row_size)
        return (clicked_row, clicked_column)

    def get_x_y_coordinate(self, row, col):
        x = (col* DIMENSION_OF_EACH_SQUARE)
        y = ((2-row)*DIMENSION_OF_EACH_SQUARE)
        return (x,y)

    def draw_xs_os(self, event, x_or_o):
        x, y = self.get_clicked_row_column(event)
        if x_or_o:
            x0, y0 = self.calculate_coordinate(x,y)
            if x_or_o == 'X':
                self.canvas.create_line(x0-(.8*DIMENSION_OF_EACH_SQUARE/2),y0-(.8*DIMENSION_OF_EACH_SQUARE/2),x0+(.8*DIMENSION_OF_EACH_SQUARE/2), y0+(.8*DIMENSION_OF_EACH_SQUARE/2),width=2.0, fill=self.x_color, tags='occupied')#down to right
                self.canvas.create_line(x0+(.8*DIMENSION_OF_EACH_SQUARE/2),y0-(.8*DIMENSION_OF_EACH_SQUARE/2),x0-(.8*DIMENSION_OF_EACH_SQUARE/2), y0+(.8*DIMENSION_OF_EACH_SQUARE/2),width=2.0, fill=self.x_color, tags='occupied')#down to right
            elif x_or_o=='O':
                self.canvas.create_oval(x0-(.8*DIMENSION_OF_EACH_SQUARE/2),y0-(.8*DIMENSION_OF_EACH_SQUARE/2),x0+(.8*DIMENSION_OF_EACH_SQUARE/2),y0+(.8*DIMENSION_OF_EACH_SQUARE/2), outline=self.o_color, width=2.0, tags='occupied')

    def calculate_coordinate(self, row, col):
        x0 = (col*DIMENSION_OF_EACH_SQUARE)+ int(DIMENSION_OF_EACH_SQUARE/2)
        y0 = ((2-row)*DIMENSION_OF_EACH_SQUARE)+int(DIMENSION_OF_EACH_SQUARE/2)
        return(x0,y0)

    def clear_board(self):
        self.canvas.delete("occupied")

    def start_new_game(self):
        self.clear_board()

def main(controller):
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    View(root, controller)
    root.mainloop()

def init_new_game():
    game_controller = controller.Controller()
    main(game_controller)

if __name__ == "__main__":
    init_new_game()
