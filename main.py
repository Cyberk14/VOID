import time

Time = (lambda: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))()
print(Time)
