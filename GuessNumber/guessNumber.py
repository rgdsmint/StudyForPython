import random

def guess():
    num = random.randint(0,10)
    flag = 1
    while True:
        try:
            guessNum = int(input('请输入你想的数:'))
        except:
            exit('输入有误')
        if guessNum == num:
            print('恭喜你,猜对了!答案就是%d.'%(num))
            print('你猜了%d次.'%(flag))
            message = input('是否继续游戏? [y/n]').lower()
            if message == 'y':
                print('-'*20)
                break
            elif message == 'n':
                print('已正常退出.')
                exit()
            else:
                exit('您输入了无法判别的元素, 游戏已停止.')
        elif guessNum > num:
            print('你猜大了')
            flag+=1
        else:
            print('你猜小了')
            flag+=1


if __name__ == '__main__':
    while True:
        guess()