import turtle as t


class peppaPig:
    '''画出小猪佩奇'''
    def __init__(self):
        self.settings()
        self.TheWholePig()

    def settings(self):
        '''设置颜色,粗细等参数等参数'''
        t.pensize(4)
        t.hideturtle()
        t.colormode(255)
        t.color((255, 155, 192), "pink")
        t.setup(840, 500)
        t.speed(10)

    def TheWholePig(self):
        '''优雅地调用绘制各个猪器官的方法 画出整只猪'''
        self.nose()
        self.head()
        self.ears()
        self.eyes()
        self.cheek()
        self.mouth()
        self.body()
        self.hands()
        self.feet()

    def nose(self):
        '''画出猪的鼻子'''
        t.pu()
        t.goto(-100, 100)
        t.pd()
        t.seth(-30)
        t.begin_fill()
        a = 0.4
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                t.lt(3)
                t.fd(a)
            else:
                a = a - 0.08
                t.lt(3)
                t.fd(a)
        t.end_fill()

        t.pu()
        t.seth(90)
        t.fd(25)
        t.seth(0)
        t.fd(10)
        t.pd()
        t.pencolor(255, 155, 192)
        t.seth(10)
        t.begin_fill()
        t.circle(5)
        t.color(160, 82, 45)
        t.end_fill()
        t.pu()
        t.seth(0)
        t.fd(20)
        t.pd()
        t.pencolor(255, 155, 192)
        t.seth(10)
        t.begin_fill()
        t.circle(5)
        t.color(160, 82, 45)
        t.end_fill()

    def head(self):
        '''画出猪的头'''
        t.color((255, 155, 192), "pink")
        t.pu()
        t.seth(90)
        t.fd(41)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.begin_fill()
        t.seth(180)
        t.circle(300, -30)
        t.circle(100, -60)
        t.circle(80, -100)
        t.circle(150, -20)
        t.circle(60, -95)
        t.seth(161)
        t.circle(-300, 15)
        t.pu()
        t.goto(-100, 100)
        t.pd()
        t.seth(-30)
        a = 0.4
        for i in range(60):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                t.lt(3)
                t.fd(a)
            else:
                a = a - 0.08
                t.lt(3)
                t.fd(a)
        t.end_fill()

    def ears(self):
        '''画出猪的耳朵'''
        t.color((255, 155, 192), "pink")
        t.pu()
        t.seth(90)
        t.fd(-7)
        t.seth(0)
        t.fd(70)
        t.pd()
        t.begin_fill()
        t.seth(100)
        t.circle(-50, 50)
        t.circle(-10, 120)
        t.circle(-50, 54)
        t.end_fill()
        t.pu()
        t.seth(90)
        t.fd(-12)
        t.seth(0)
        t.fd(30)
        t.pd()
        t.begin_fill()
        t.seth(100)
        t.circle(-50, 50)
        t.circle(-10, 120)
        t.circle(-50, 56)
        t.end_fill()

    def eyes(self):
        '''画出猪的眼睛'''
        t.color((255, 155, 192), "white")
        t.pu()
        t.seth(90)
        t.fd(-20)
        t.seth(0)
        t.fd(-95)
        t.pd()
        t.begin_fill()
        t.circle(15)
        t.end_fill()

        t.color("black")
        t.pu()
        t.seth(90)
        t.fd(12)
        t.seth(0)
        t.fd(-3)
        t.pd()
        t.begin_fill()
        t.circle(3)
        t.end_fill()

        t.color((255, 155, 192), "white")
        t.pu()
        t.seth(90)
        t.fd(-25)
        t.seth(0)
        t.fd(40)
        t.pd()
        t.begin_fill()
        t.circle(15)
        t.end_fill()

        t.color("black")
        t.pu()
        t.seth(90)
        t.fd(12)
        t.seth(0)
        t.fd(-3)
        t.pd()
        t.begin_fill()
        t.circle(3)
        t.end_fill()

    def cheek(self):
        '''画出猪的脸颊'''
        t.color((255, 155, 192))
        t.pu()
        t.seth(90)
        t.fd(-95)
        t.seth(0)
        t.fd(65)
        t.pd()
        t.begin_fill()
        t.circle(30)
        t.end_fill()

    def mouth(self):
        '''画出猪的嘴'''
        t.color(239, 69, 19)
        t.pu()
        t.seth(90)
        t.fd(15)
        t.seth(0)
        t.fd(-100)
        t.pd()
        t.seth(-80)
        t.circle(30, 40)
        t.circle(40, 80)

    def body(self):
        '''画出猪的身体'''
        t.color("red", (255, 99, 71))
        t.pu()
        t.seth(90)
        t.fd(-20)
        t.seth(0)
        t.fd(-78)
        t.pd()
        t.begin_fill()
        t.seth(-130)
        t.circle(100, 10)
        t.circle(300, 30)
        t.seth(0)
        t.fd(230)
        t.seth(90)
        t.circle(300, 30)
        t.circle(100, 3)
        t.color((255, 155, 192), (255, 100, 100))
        t.seth(-135)
        t.circle(-80, 63)
        t.circle(-150, 24)
        t.end_fill()

    def hands(self):
        '''画出猪的手'''
        t.color((255, 155, 192))
        t.pu()
        t.seth(90)
        t.fd(-40)
        t.seth(0)
        t.fd(-27)
        t.pd()
        t.seth(-160)
        t.circle(300, 15)
        t.pu()
        t.seth(90)
        t.fd(15)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.seth(-10)
        t.circle(-20, 90)

        t.pu()
        t.seth(90)
        t.fd(30)
        t.seth(0)
        t.fd(237)
        t.pd()
        t.seth(-20)
        t.circle(-300, 15)
        t.pu()
        t.seth(90)
        t.fd(20)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.seth(-170)
        t.circle(20, 90)

    def feet(self):
        '''画出大猪蹄子'''
        t.pensize(10)
        t.color((240, 128, 128))
        t.pu()
        t.seth(90)
        t.fd(-75)
        t.seth(0)
        t.fd(-180)
        t.pd()
        t.seth(-90)
        t.fd(40)
        t.seth(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)

        t.pensize(10)
        t.color((240, 128, 128))
        t.pu()
        t.seth(90)
        t.fd(40)
        t.seth(0)
        t.fd(90)
        t.pd()
        t.seth(-90)
        t.fd(40)
        t.seth(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)

    def tail(self):
        '''画出猪的小尾巴'''
        t.pensize(4)
        t.color((255, 155, 192))
        t.pu()
        t.seth(90)
        t.fd(70)
        t.seth(0)
        t.fd(95)
        t.pd()
        t.seth(0)
        t.circle(70, 20)
        t.circle(10, 330)
        t.circle(70, 30)
        t.done()


if __name__ == '__main__':
    peppa = peppaPig()