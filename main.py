from tkinter import *
from game import Game
from settings import *
from objects import *
from PIL import ImageTk, Image

tk = Tk()
tk.title(GAME_NAME)
tk.resizable(0, 0) #как можно сдвинуть окно
tk.wm_attributes('-topmost', 1) #поверх всех окон

canvas = Canvas(tk, width=WIDHT, height=HEIGHT, highlightthickness=0) #создание "холста"
canvas.pack() #менеждер геометрии

#создание фона
bg = PhotoImage(file='bg1.gif')
w = bg.width()
h = bg.height()
for x in range(2):
    for y in range(2):
        canvas.create_image(x * w, y * h, image=bg, anchor='nw')

tk.update() #обрабатывает все задачи, стоящие в очереди

game = Game(tk, canvas)

if __name__ == '__main__':
    game.game_run()
