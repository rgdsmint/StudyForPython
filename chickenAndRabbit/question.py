# 有鸡兔若干  上三十五头  下九十四足  问鸡兔各几何

import time


def chicken_rabbit_1(head, foot):
    # 穷举
    for chicken in range(0, head + 1):
        for rabbit in range(0, head - chicken + 1):
            if chicken + rabbit == head and chicken * 2 + rabbit * 4 == foot:
                print('鸡的只数为%d , 兔子有%d' % (chicken, rabbit))


def chicken_rabbit_2(head, foot):
    ''' 中二算法 : 
        一群鸡和一群兔子站在一起, 我说"pia", 就都抬起一条腿,
        第一次"pia!" 剩下一条腿的鸡若干以及一腿朝天的兔纸,
        第二次"pia!" 鸡鸡们全倒地上了, 这时只剩下了剩下腿数量的一半数量的兔兔们了!
    '''
    rabbit = (foot - 2 * head) / 2
    chicken = head - rabbit
    print('鸡的只数为%d , 兔子有%d' % (chicken, rabbit))


if __name__ == '__main__':
    start = time.time()
    # 底下这个数 穷举会死翘翘的
    chicken_rabbit_2(50000000, 150000000)
    end = time.time()
    print(end - start)
