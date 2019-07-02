
import time

scale = 60
startTime = time.perf_counter()
print("执行开始".center(scale // 2, "-"))
for i in range(scale + 1):
    stars = "*" * i
    points = "." * (scale - i)
    persent = (i / scale) * 100
    passTime = time.perf_counter() - startTime
    print("\r{:^3.0f}%[{}->{}]{:.2f}s"
            .format(persent, stars, points, passTime), end="")
    time.sleep(0.1)

print("\n" + "执行结束".center(scale // 2, "-"))
                    
                    
