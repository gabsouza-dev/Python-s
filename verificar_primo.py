def verificar_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Digite um número para verificar se é primo: "))

if verificar_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
