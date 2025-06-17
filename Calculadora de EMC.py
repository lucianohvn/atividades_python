def calcular_energia(massa):
    c = 3e8  # velocidade da luz em m/s
    energia = massa * c ** 2
    return energia

def main():
    try:
        massa = float(input("Digite a massa em kg: "))
        energia = calcular_energia(massa)
        print(f"A energia equivalente é: {energia:.2e} joules")
    except ValueError:
        print("Por favor, insira um valor numérico válido para a massa.")

if __name__ == "__main__":
    main()