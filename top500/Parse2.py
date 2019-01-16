
def getChina():
    name = []
    with open(
            'E:\\pythonDemo\\top500\\ownedCountry.txt', 'r',
            encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line:
                line = line.rstrip()
                name.append(line)
    names = name[:]

    indexes = []
    flag = 0
    for name in names:
        if name == '中国':
            indexes.append(flag)
            flag += 1
            continue
        flag += 1
    turnoverOfChina = 0
    turnoverOfRound_list = []
    with open('E:\\pythonDemo\\top500\\turnover.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line:
                if '，' in line:
                    line = float(line.rstrip().replace('，', ''))
                else:
                    line = float(line.rstrip())
                turnoverOfRound_list.append(line)
    turnoverOfChina_list = []
    for index in indexes:
        turnoverOfChina_list.append(turnoverOfRound_list[index])
    temp = 0
    for turnover_china in turnoverOfChina_list:
        temp += turnover_china
    turnoverOfChina = temp
    return turnoverOfChina

def getAmerica():
    name = []
    with open(
            'E:\\pythonDemo\\top500\\ownedCountry.txt', 'r',
            encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line:
                line = line.rstrip()
                name.append(line)
    names = name[:]

    indexes = []
    flag = 0
    for name in names:
        if name == '美国':
            indexes.append(flag)
            flag += 1
            continue
        flag += 1
    turnoverOfAmerica = 0
    turnoverOfRound_list = []
    with open('E:\\pythonDemo\\top500\\turnover.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line:
                if '，' in line:
                    line = float(line.rstrip().replace('，', ''))
                else:
                    line = float(line.rstrip())
                turnoverOfRound_list.append(line)
    turnoverOfAmerica_list = []
    for index in indexes:
        turnoverOfAmerica_list.append(turnoverOfRound_list[index])
    temp = 0
    for turnover_America in turnoverOfAmerica_list:
        temp += turnover_America
    turnoverOfAmerica = temp

    return turnoverOfAmerica


def getRound():
    turnoverOfRound_list = []
    with open('E:\\pythonDemo\\top500\\turnover.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line:
                if '，' in line:
                    line = float(line.rstrip().replace('，', ''))
                else:
                    line = float(line.rstrip())
                turnoverOfRound_list.append(line)
    turnoverOfRound = 0
    temp = 0
    for turnover in turnoverOfRound_list:
        temp += turnover
    turnoverOfRound = temp

    return turnoverOfRound

a = getRound()
b = getAmerica()
c = getChina()
print(a)
print(b)
print(c)


print('--------------')
print(a - b - c)