def calculadora():
    while True:
        print("## CALCULADORA ##\n")
        print("1. soma")
        print("2. subtração")
        print("3. multiplicação")
        print("4. divisão")
        print("5. resto da divisão")
        print("6. sair")
        
        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            print("1. soma")
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = num1 + num2
            print("A soma dos valores: ", resultado, "\n")
        
        elif opcao == 2:
            print("2. subtração")
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = num1 - num2
            print("A subtração dos valores: ", resultado)

        elif opcao == 3:
            print("3. multiplicação")
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = num1 * num2
            print("A multiplicação dos valores: ", resultado)

        elif opcao == 4:
            print("4. divisão")
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            if num2 != 0:
                resultado = num1 / num2
                print("A divisão dos valores: ", resultado)
            else:
                print("Erro: Divisão por zero.")

        elif opcao == 5:
            print("5. resto da divisão")
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            if num2 != 0:
                resultado = num1 % num2
                print("O resto da divisão dos valores: ", resultado)
            else:
                print("Erro: Divisão por zero.")

        elif opcao == 6:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    
    calculadora()