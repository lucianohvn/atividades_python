def ano_bissexto(ano):
    # Um ano é bissexto se:
    # 1. É divisível por 4 e não é divisível por 100, exceto se for divisível por 400.
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Leitura do ano do usuário
ano = int(input("Digite um ano: "))

# Verificação se o ano é bissexto
if ano_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
        print(f"O ano {ano} não é bissexto.")