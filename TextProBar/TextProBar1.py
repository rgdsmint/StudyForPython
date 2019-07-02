#文本进度条
import time

scale = 10
print("------执行开始------")
for i in range(scale + 1):
    stars = "*" * i
    points = "." * (scale - i)
    persent = (i / scale) * 100
    print("{:^3.0f}%[{}->{}]".format(persent, stars, points))
    time.sleep(0.1)

print("------执行结束-------")
