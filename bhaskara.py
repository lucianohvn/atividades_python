import math

def calcular_raizes(a, b, c):
    # Calcula o discriminante (delta)
    delta = b**2 - 4*a*c

    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        # Uma única raiz real
        raiz = -b / (2 * a)
        return f"A equação possui uma única raiz real: {raiz:.2f}"
    else:
        # Duas raízes reais
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}"

# Leitura dos coeficientes a, b e c do usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Verifica se a é zero para garantir que não é uma equação de primeiro grau
if a == 0:
    print("O coeficiente a não pode ser zero em uma equação de segundo grau.")
else:
    # Calcula e exibe as raízes
    resultado = calcular_raizes(a, b, c)
    print(resultado)