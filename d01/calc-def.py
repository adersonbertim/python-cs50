def main():
    x = int(input("Square number? "))
    print("Square of your number is: ", square(x))


def square(n):
    return pow(n, 2)

main()
