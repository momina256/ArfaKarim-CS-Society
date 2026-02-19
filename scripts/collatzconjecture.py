n = 3
while True:
    if n / 2 == 0:
        n = 3 * n + 1 
    elif n != 0:
        n = n / 2
    elif n == 1:
        print("Success!")
