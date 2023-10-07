def main():
    x = int(input("What's number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
# Uma maneira mais elegante seria "return n % 2 == 0"
main()
# Basicamente usando a função main pegamos um numero
# Na função is_even esse numero é usado com o operador de modulus, usando o == se for 0 retorna True se não False.
