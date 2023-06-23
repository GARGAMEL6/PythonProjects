import tkinter as tk
import random


class MyButton(tk.Button):
    def __init__(self, master, x, y, *args, **kwargs):
        super(MyButton, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.color = random.choice(Game.COLORS)

    def __repr__(self):
        return f'MyButton {self.x} {self.y} {self.color}'


class Game:
    win = tk.Tk()
    win.geometry(f"1000x700")
    ROWS = 10
    COLUMNS = 10
    COLORS = ['red', 'green', 'blue', 'yellow']

    SCORE = 0
    STEPS = 20

    is_click = False

    Button = ''

    tk.Label(win, text=f'Score: {SCORE}', font='Calibri 20 bold').grid(row=1, column=COLUMNS + 1)
    tk.Label(win, text=f' Steps: {STEPS}', font='Calibri 20 bold').grid(row=2, column=COLUMNS + 1)

    def __init__(self):
        self.buttons = []
        self.colors = []
        for i in range(Game.ROWS):
            temp = []
            color = []
            for j in range(Game.COLUMNS):
                btn = MyButton(Game.win, x=i, y=j, width=3, text='●', font=f'Calibri 15 bold', bg='#66FFB2',
                               activebackground='#66FFB2')
                btn.config(command=lambda button=btn: self.click(button))
                btn['fg'] = btn.color
                btn['activeforeground'] = btn.color
                temp.append(btn)
                color.append(btn.color)
            self.buttons.append(temp)
            self.colors.append(color)

    def click(self, clicked_button: MyButton):
        if self.is_click:
            temp = clicked_button.color
            self.buttons[clicked_button.x][clicked_button.y].color = self.Button.color
            self.colors[clicked_button.x][clicked_button.y] = self.Button.color
            self.buttons[self.Button.x][self.Button.y].color = temp
            self.colors[self.Button.x][self.Button.y] = temp
            self.STEPS -= 1

            tk.Label(Game.win, text=f' Steps: {Game.STEPS}', font='Calibri 20 bold').grid(row=2, column=Game.COLUMNS + 1)
            self.is_click = False
        else:
            self.Button = clicked_button
            self.is_click = True
        print(clicked_button.x, clicked_button.y)
        self.create_buttons()

    def if_zero(self):
        for i in range(Game.ROWS):
            for j in range(Game.COLUMNS):
                btn = self.buttons[i][j]
                if btn.color == 'black':
                    if i == 0:
                        btn.color = random.choice(Game.COLORS)
                        self.colors[i][j] = btn.color
                    else:
                        btn.color = self.buttons[i - 1][j].color
                        self.colors[i][j] = btn.color
                        self.buttons[i - 1][j].color = 'black'
                        self.colors[i - 1][j] = 'black'

    def zeros_search(self):
        for i in range(Game.ROWS - 1, -1, -1):
            while 'black' in self.colors[i]:
                self.if_zero()

    def repeat_search(self):
        for i in range(Game.ROWS):
            f = False
            j_begin = 0
            for j in range(1, Game.COLUMNS - 1):
                if self.colors[i][j] == self.colors[i][j - 1] == self.colors[i][j + 1]:
                    f = True
                    j_begin = j - 1
                else:
                    if f:
                        while j_begin <= j:
                            self.colors[i][j_begin] = 'black'
                            self.buttons[i][j_begin].color = 'black'
                            j_begin += 1
                        f = False
            if f:
                while j_begin < Game.COLUMNS:
                    self.colors[i][j_begin] = 'black'
                    self.buttons[i][j_begin].color = 'black'
                    j_begin += 1

        for j in range(Game.COLUMNS):
            f = False
            i_begin = 0
            for i in range(1, Game.ROWS - 1):
                if self.colors[i][j] == self.colors[i - 1][j] == self.colors[i + 1][j]:
                    f = True
                    i_begin = i - 1
                else:
                    if f:
                        while i_begin <= j:
                            self.colors[i_begin][j] = 'black'
                            self.buttons[i_begin][j].color = 'black'
                            i_begin += 1
                        f = False
            if f:
                while i_begin < Game.COLUMNS:
                    self.buttons[i_begin][j].color = 'black'
                    i_begin += 1

    def create_buttons(self):
        for _ in range(10):
            self.repeat_search()
            self.zeros_search()
        for i in range(Game.ROWS):
            for j in range(Game.COLUMNS):
                btn = self.buttons[i][j]
                btn.color = self.colors[i][j]
                btn['fg'] = btn.color
                btn['activeforeground'] = btn.color
                btn.grid(row=i, column=j)

    def print_buttons(self):
        for row_btn in self.colors:
            print(row_btn)

    def start(self):
        self.create_buttons()
        self.print_buttons()
        Game.win.mainloop()


game = Game()
game.start()
