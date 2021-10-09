def puzzle(a, n) :
    s = " "
    while a > 0:
        s = str(a % n) + s
        a //= n
    print(s)


a = input("Введите число:")
try:
    a = int(a)
    n = input("Введите целевую систему счисления:")
    try:
       n = int(n)
       if (n == 2 and 0 < a <= 255) or n == 8:
        puzzle(a, n)
       else :
            print("Введена неправильная система счисления.")
            quit()
    except ValueError :
            print("Введено не число.")
except ValueError :
    print("Введено не число.")
