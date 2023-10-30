def calculadora():
    numero1 = float(input("Digite o primeiro numero:"))
    numero2 = float(input("Digite o segundo numero:"))

    operador = input("Digite o operador(+, - *, /):")

    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2

    else:
        print("Operador inválido")
        return
    print("O resultado é", resultado)

calculadora()