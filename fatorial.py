def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

num = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {num} é {fatorial(num)}")