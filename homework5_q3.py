def main():
    age = int(input("Enter your age: "))
    
    if age > 100:
        print("Congratulations! You appear on the Smucker's jar.")
    elif age >= 65:
        print("You are a senior.")
    elif age >= 20:
        print("You are an adult.")
    elif age >= 13:
        print("You are a teenager.")
    elif age >= 0:
        print("You are a child.")
    else:
        print("Invalid age.")



main()