# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 34.9:
        return "Sobrepeso"
    else:  # IMC >= 35
        return "Obesidade"

# Leitura do peso e altura do usuário
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Classificação do IMC
classificacao = classificar_imc(imc)

# Exibição do resultado
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")