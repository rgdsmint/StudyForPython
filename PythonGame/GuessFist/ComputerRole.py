import random


class computerRole:
    '''定义一个电脑玩家'''

    def __init__(self):
        '''设置各种属性'''
        
        self.name = ""
        self.fisting = ['准备好结束正义的审判吧！', 'You are dying.', '天降正义！', 'no way!']
        self.win = ['臣服于我吧！', "I'm winner!", '你得听我的。', 'You are loser!']
        self.lose = ['甘拜下风。', '你很强！', '愿听教诲。', '悉听尊便']
        # 1 jiandao 2 shitou 3 bu
        self.fist = None
        self.score = 0

    def lines(self, state):
        '''设置各个场景会说的台词'''

        rand_num = random.randint(0, 3)
        if state == -1:
            return self.lose[rand_num]
        elif state == 0:
            return self.win[rand_num]
        else:
            return self.fisting[rand_num]

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getFist(self):
        return self.fist

    def setFist(self, fist):
        self.fist = fist

    def getScore(self):
        return self.score

    def setScore(self):
        self.score += 1