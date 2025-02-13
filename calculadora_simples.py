def calculadora():
    print("Calculadora Simples")
    print("Operações disponíveis: +, -, *, /")
    
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2 if num2 != 0 else "Erro! Divisão por zero."
    else:
        resultado = "Operação inválida!"

    print(f"Resultado: {resultado}")

calculadora()
