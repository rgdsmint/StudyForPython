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

# print(name)
print()
print()
print()
print()
print()
print()
print()
print()
print()
same = name[:]
for item in name:
    if item == '美国':
        same.remove('美国')
    elif item == '中国':
        same.remove('中国')
    elif item == '日本':
        same.remove('日本')
    elif item == '德国':
        same.remove('德国')
    elif item == '法国':
        same.remove('法国')
    elif item == '英国':
        same.remove('英国')
    elif item == '印度':
        same.remove('印度')
    elif item == '巴西':
        same.remove('巴西')
    elif item == '意大利':
        same.remove('意大利')
    elif item == '加拿大':
        same.remove('加拿大')
    elif item == '韩国':
        same.remove('韩国')
    elif item == '俄罗斯':
        same.remove('俄罗斯')
    elif item == '荷兰':
        same.remove('荷兰')
    elif item == '瑞士':
        same.remove('瑞士')
    elif item == '新加坡':
        same.remove('新加坡')
    elif item == '爱尔兰':
        same.remove('爱尔兰')                      
    elif item == '墨西哥':
        same.remove('墨西哥')    
    elif item == '西班牙':
        same.remove('西班牙')
    elif item == '澳大利亚':
        same.remove('澳大利亚')
    elif item == '瑞典':
        same.remove('瑞典')
name = same[:]
print(name)
print(len(name))
print('美国' in name)
America = 0
china = 0
japan = 0
Germany = 0
france = 0
England = 0
india = 0
Brazil = 0
Italy = 0
Canada = 0
southKorea = 0
russia = 0
Netherlands = 0
switzerland = 0
singapore = 0 
Ireland = 0
mexico = 0
spain = 0
Australia = 0
sweden = 0
others = 0
for item in names:
    if item == '美国':
        America += 1
    elif item == '中国':
        china += 1
    elif item == '日本':
        japan += 1
    elif item == '德国':
        Germany += 1
    elif item == '法国':
        france += 1
    elif item == '英国':
        England += 1
    elif item == '印度':
        india += 1
    elif item == '巴西':
        Brazil += 1
    elif item == '意大利':
        Italy += 1
    elif item == '加拿大':
        Canada += 1
    elif item == '韩国':
        southKorea += 1
    elif item == '俄罗斯':
        russia += 1
    elif item == '荷兰':
        Netherlands += 1
    elif item == '瑞士':
        switzerland += 1
    elif item == '新加坡':
        singapore += 1
    elif item == '爱尔兰':
        Ireland += 1
    elif item == '墨西哥':
        mexico += 1
    elif item == '西班牙':
        spain += 1
    elif item == '澳大利亚':
        Australia += 1
    elif item == '瑞典':
        sweden += 1
    else:
        others += 1

print(
    '美国:{}\n中国:{}\n日本:{}\n德国:{}\n法国:{}\n英国:{}\n印度:{}\n巴西:{}\n意大利:{}\n加拿大:{}\n韩国:{}\n俄罗斯:{}\n荷兰:{}\n瑞士:{}\n新加坡:{}\n爱尔兰:{}\n墨西哥:{}\n西班牙:{}\n澳大利亚:{}\n瑞典:{}\n其他:{}'.
    format(America, china, japan, Germany, france, England, india, Brazil,
           Italy, Canada, southKorea, russia, Netherlands, switzerland,
           singapore, Ireland, mexico, spain, Australia, sweden, others))
# a = input()
count = [America, china, japan, Germany, france, England, india
        , Brazil, Italy, Canada, southKorea, russia, Netherlands
        , switzerland, singapore, Ireland, mexico, spain, Australia
        , sweden]

count = sorted(count)
print(count)