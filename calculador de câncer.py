def calcular_perda_de_vida(cigarros_por_dia, anos_fumando):
    minutos_por_cigarro = 10
    dias_por_ano = 365
    total_cigarros = cigarros_por_dia * dias_por_ano * anos_fumando
    total_minutos_perdidos = total_cigarros * minutos_por_cigarro
    total_dias_perdidos = total_minutos_perdidos / (24 * 60)
    return total_dias_perdidos

try:
    cigarros_por_dia = int(input("Informe a quantidade de cigarros fumados por dia: "))
    anos_fumando = int(input("Informe quantos anos você fumou: "))

    dias_perdidos = calcular_perda_de_vida(cigarros_por_dia, anos_fumando)

    print(f"Você irá perder aproximadamente {dias_perdidos:.2f} dias de vida.")
except ValueError:
    print("Por favor, insira valores válidos.")