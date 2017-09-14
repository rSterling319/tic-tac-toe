import sys
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.colorchooser import *
from configparser import ConfigParser

import config

class PreferencesWindow():
    def __init__(self, view):
        self.parent = view.parent
        self.fill_preference_colors()
        self.view = view
        self.create_prefereces_window()

    def fill_preference_colors(self):
        self.x_color = config.X_COLOR
        self.o_color = config.O_COLOR
        self.board_color = config.BOARD_COLOR

    def set_x_color(self):
        self.x_color = askcolor(initialcolor=self.x_color)[-1]

    def set_o_color(self):
        self.o_color = askcolor(initialcolor=self.o_color)[-1]

    def set_board_color(self):
        self.board_color = askcolor(initialcolor=self.board_color)[-1]

    def create_prefereces_window(self):
        self.pref_window= tk.Toplevel(self.parent)
        self.pref_window.title("set Tic-Tac-Toe preferences")
        self.create_prefereces_list()
        self.pref_window.transient(self.parent)

    def create_prefereces_list(self):
        tk.Label(self.pref_window, text='X Color').grid(row=1, sticky='w', padx=5, pady=5)
        tk.Label(self.pref_window, text='O Color').grid(row=2, sticky='w', padx=5, pady=5)
        tk.Label(self.pref_window, text='Board Color').grid(row=3, sticky='w',padx=5, pady=5)
        self.x_color_button = tk.Button(self.pref_window, text='Select X Color', command=self.set_x_color)
        self.x_color_button.grid(row=1,column=1,columnspan=2,sticky='e',padx=5,pady=5)
        self.o_color_button = tk.Button(self.pref_window, text='Select O Color', command=self.set_o_color)
        self.o_color_button.grid(row=2, column=1, columnspan=2, sticky='e',padx=5,pady=5)
        self.board_color_button = tk.Button(self.pref_window, text='Select Board Color', command=self.set_board_color)
        self.board_color_button.grid(row=3, column=2, columnspan=2, sticky='e', padx=5, pady=5)
        tk.Button(self.pref_window, text="Save", command=self.on_save_button_clicked).grid(row=4,column=2, sticky='e', padx=5, pady=5)
        tk.Button(self.pref_window, text='Cancel', command=self.on_cancel_button_clicked).grid(row=4, column=1, sticky='e', padx=5, pady=5)

    def on_save_button_clicked(self):
        self.set_new_values()
        self.pref_window.destroy()
        self.view.reload_colors(self.x_color, self.o_color, self.board_color)

    def set_new_values(self):
        configure = ConfigParser()
        configure.read('tic_tac_toe_options.ini')
        configure.set('tic_tac_toe_colors','x_color', self.x_color)
        configure.set('tic_tac_toe_colors','o_color', self.o_color)
        configure.set('tic_tac_toe_colors','board_color', self.board_color)
        config.X_COLOR = self.x_color
        config.O_COLOR = self.o_color
        config.BOARD_COLOR = self.board_color
        with open('tic_tac_toe_options.ini', 'w')as config_file:
            configure.write(config_file)
    def on_cancel_button_clicked(self):
        self.pref_window.destroy()
