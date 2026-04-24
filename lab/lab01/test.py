y = 0
x = 0
for i in range(len(str(y))):
    x = x + y % 10
    y = y // 10
print(x)