import random
from settings import *

class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score

        self.id = canvas.create_oval(SIZE_BALL, fill=color)  # создание шарика
        self.canvas.move(self.id, *START_POS_BALL)  # перемещение в (250, 100)

        #создание ситуации с различными направлениями движения в начале игры
        start_move_ball = [-2, 2] 
        random.shuffle(start_move_ball)

        self.x = start_move_ball[0]
        self.y = -2

        #узнаём значение высоты и ширины
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        #проверка столкновения шарика и платформы
        if pos[2] >=  paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                
                self.score.add_point() #увеличение очков
                return True

        return False

    def draw(self): #отрисовка
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0: #столкновение с потолком
            self.y = self.score.speed_dif()

        if pos[3] >= self.canvas_height: #столкновение с полом
            self.hit_bottom = True
            self.canvas.create_text(PLACE_GAME_OVER_TEXT, text=GAME_OVER_TEXT, font=FONT_GAME_OVER_TEXT, fill=COLOR_GAME_OVER_TEXT)

        if self.hit_paddle(pos): #столкновение с платформой
            self.y = -self.score.speed_dif()

        if pos[0] <= 0: #столкновение с левой стеной
            self.x = self.score.speed_dif()

        if pos[2] >= self.canvas_width: #столкновение с правой стеной
            self.x = -self.score.speed_dif()

class  Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(SIZE_PADDLE, fill=color) #создание платформы

        start_pos_paddle = [40, 60, 120, 150, 180, 200]
        random.shuffle(start_pos_paddle)

        self.start_pos_x = start_pos_paddle[0]
        self.canvas.move(self.id, self.start_pos_x, 450)

        self.x = 0
        self.canvas_width  = self.canvas.winfo_width()

    def turn_right(self, event):
        self.x = 2

    def turn_left(self, event):
        self.x = -2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0: #столкновение с левой стеной
            self.x = 0

        if pos[2] >= self.canvas_width: #столкновение с правой стеной
            self.x = 0

class Score:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.score = 0
        self.id = canvas.create_text(PLACE_SCORE_TEXT, text='Score: ' + str(self.score), font=FONT_SCORE_TEXT, fill=color)
    
    def speed_dif(self):
        if 3 <= self.score < 5:
            return 3
        elif 5 <= self.score < 7:
            return 4
        elif self.score >= 7:
            return 5
        else:
            return 2

    def add_point(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text='Score: ' + str(self.score)) #изменение очков на холсте
        self.speed_dif()
