a = [7, 9, 11, 13, 15, 20, 23]

x = []
for num in a:
    for m in range(2, num//2):
        if (num % m)==0:
            break
    else:
        print('This is prime', num)
        x.append(num)
print(x)
