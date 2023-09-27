# def é como nomeamos nossa propria função dentro do codigo

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello",to)

main()
