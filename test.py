def is_increase(n):
    a = 0
    b = n % 10
    n//=10
    check = True
    while n > 0:
        a = n % 10
        print(a)
        print(b)
        if b < a: check = False
        b = a
        n//=10
    if check: return False
    else: return True
is_increase(12345678888888888888889)