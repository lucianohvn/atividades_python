def calculadora():
    print("Selecione a operação: ")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    opcao= int(input("Digite sua opção 1,2,3,4: "))

    if opcao in [1, 2, 3 , 4]:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))

    if opcao == 1:
        resultado = num1 + num2
        print("A soma dos valores: ", resultado)
    elif opcao == 2:
        resultado: num1 - num2 # type: ignore
        print("A subtração dos valores: ", resultado)
    elif opcao == 3:
        resultado = num1 * num2
        print("A multiplicação dos valores: ", resultado)
    elif opcao == 4:
        resultado = num1 / num2 
        print("A divisão dos valores é de: ", resultado)
    else:
        print("Erro: divisão por zero não é permitido.")
        print("Opcão inválida. Tente novamente.")

        print("Este é o fim da calculadora.")
calculadora()