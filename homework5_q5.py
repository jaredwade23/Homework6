def isPrime(n):
    found = False

    for i in range(2, n):
        if n % i == 0:
            found = True


    return found



def main():
    n = int(input("Enter a number: "))

    found = isPrime(n)

    if found:
        print(n, "is not a prime number.")
    else:
        print(n, "is a prime number.")


main()