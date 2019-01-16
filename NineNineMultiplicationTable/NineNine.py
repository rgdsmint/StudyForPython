def jiujiu():
    for item in range(1, 10):
        for line in range(1, item + 1):
            print('%d * %d = %d\t' % (line, item, line * item), end='')
        print()


if __name__ == '__main__':
    jiujiu()