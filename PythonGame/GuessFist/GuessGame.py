from humanRole import humanRole
from computerRole import computerRole
import random
import time
import sys


class Guess:
    '''定义一个游戏房间'''

    def __init__(self):
        '''
        实例化两个玩家
        一个人类玩家
        以及一个电脑玩家
        '''

        self.player1 = humanRole()
        self.player2 = computerRole()

    def rule(self, fist):
        '''
        设定规则
        1 为剪刀
        2 为石头
        3 为布
        '''

        if fist == 1:
            return '剪刀'
        elif fist == 2:
            return '石头'
        else:
            return '布'

    def loading(self):
        '''实现加载过程(伪)'''
        scale = 60
        print("游戏加载".center(scale // 2, "-"))
        startTime = time.perf_counter()
        for i in range(scale + 1):
            stars = "*" * i
            points = "." * (scale - i)
            persent = (i / scale) * 100
            passTime = time.perf_counter() - startTime
            print("\r{:^3.0f}%[{}->{}]{:.2f}s"
                .format(persent, stars, points, passTime), end="")
            time.sleep(0.1)
        print("\n" + "加载完成".center(scale // 2, "-"))

    def menu(self):
        '''显示规则菜单'''

        print("1:剪刀")
        print("2:石头")
        print("3：布")

    def chooseRole(self):
        '''选择角色'''

        role = ['艾伦.耶格尔', '三笠.阿克曼', '佐佐木琲世', '金木研一', '白马探']
        player1_name = input('请输入你的名字:')
        self.player1.setName(player1_name)
        player2_name = role[random.randint(0, 4)]
        self.player2.setName(player2_name)
        print('%s VS %s' % (player1_name, player2_name))

    def fisting(self):
        '''出拳'''

        fist1 = int(input("请出拳:"))
        self.player1.setFist(fist1)
        print("[%s]:%s" % (self.player1.getName(),
                           self.player1.fisting[random.randint(0, 3)]))
        fist2 = random.randint(1, 3)
        self.player2.setFist(fist2)
        print("[%s]:%s" % (self.player2.getName(),
                           self.player2.fisting[random.randint(0, 3)]))

    def show(self):
        '''显示游戏日志'''

        print('[裁判]:', end="")
        print('%s出的是:%s.' % (self.player1.getName(),
                             self.rule(self.player1.getFist())))
        print('[裁判]:', end="")
        print('%s出的是:%s.' % (self.player2.getName(),
                             self.rule(self.player2.getFist())))

    def pk(self):
        '''实现判断胜负的逻辑'''

        f1 = self.player1.getFist()
        f2 = self.player2.getFist()
        if f1 == 1 and f2 == 3 or f1 == 2 and f2 == 1 or f1 == 3 and f2 == 2:
            return 1
        elif f1 == f2:
            return 0
        else:
            return -1

    def is_win_or_lose(self):
        '''判断胜负'''

        result = self.pk()
        if result == 1:
            print('[裁判]:[%s]赢一局.' % (self.player1.getName()))
            self.player1.setScore()
            print("[%s]:%s" % (self.player1.getName(),
                               self.player1.win[random.randint(0, 3)]))
            print("[%s]:%s" % (self.player2.getName(),
                               self.player2.lose[random.randint(0, 3)]))

        elif result == 0:
            print('[裁判]:平局.')
        else:
            print('[裁判]:%s赢一局.' % (self.player2.getName()))
            self.player2.setScore()
            print("[%s]:%s" % (self.player2.getName(),
                               self.player2.win[random.randint(0, 3)]))
            print("[%s]:%s" % (self.player1.getName(),
                               self.player1.lose[random.randint(0, 3)]))

    def is_continue(self):
        '''询问是否继续'''

        retu = input("是否继续？[y/n]")
        retu = retu.lower()
        if retu == "y":
            return 1
        else:
            return -1

    def gameOver(self):
        '''
        如果游戏结束  则显示此界面
        展示比分情况
        判断最终胜负
        '''

        print("[%s]:%d" % (self.player1.getName(), self.player1.getScore()))
        print("[%s]:%d" % (self.player2.getName(), self.player2.getScore()))
        if self.player1.getScore() > self.player2.getScore():
            print('[%s] 获得最终胜利.' % (self.player1.getName()))
        elif self.player1.getScore() < self.player2.getScore():
            print("[%s] 获得最终胜利." % (self.player2.getName()))
        else:
            print('平.')

    def main(self):
        '''控制代码主要逻辑顺序'''

        self.loading()
        self.chooseRole()
        while True:
            self.menu()
            self.fisting()
            self.show()
            self.is_win_or_lose()
            re = self.is_continue()
            if re == 1:
                pass
            else:
                self.gameOver()
                break


if __name__ == '__main__':
    '''运行代码'''
    
    game = Guess()
    game.main()
