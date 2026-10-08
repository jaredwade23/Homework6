def chaos(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
    print(x) 


def main():
    k = float(input("Enter the value of k: "))
    x = float(input("Enter the initial value of x (between 0 and 1): "))

    if x < 0 or x > 1:
        print("Error: x must be between 0 and 1.")
    else:
        chaos(k, x, 30)


main()