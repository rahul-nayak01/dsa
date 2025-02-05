def check_even(n):
    if n == (n>>1)<<1:
        print("Even")
    else:
        print("Odd")
    return ""
    






print(check_even(101))