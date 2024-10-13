def calcular_preco(qtd_dias, km_percorridos):
    preco_por_dia = 60.00
    preco_por_km = 0.15
    custo_total = (qtd_dias * preco_por_dia) + (km_percorridos * preco_por_km)
    return custo_total

try:
    dias_alugados = int(input("Informe a quantidade de dias que o carro foi alugado: "))
    km_percorridos = float(input("Informe a quantidade de Km percorridos: "))

    preco = calcular_preco(dias_alugados, km_percorridos)
    
    print(f"O valo total pelo aluguel do carro é: R${preco:.2f}")
except ValueError:
    print("Por favor, insira valores válidos.")