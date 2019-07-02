#计算圆周率PI 公式法
import time
start = time.perf_counter()
PI = 0
count = 10000
for k in range(count):    
    PI += 1/pow(16,k)*(4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6) )  
print("圆周率值是: {}".format(PI))
print("所用时间是: {}".format(time.perf_counter() - start))
