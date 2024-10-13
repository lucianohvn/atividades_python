def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

while True:
    print("\nSelecione a conversão desejada:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Fahrenheit para Kelvin")
    print("6. Kelvin para Fahrenheit")
    print("7. Sair")

    escolha = input("Digite o número da opção: ")

    if escolha == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
        
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")

    elif escolha == '3':
        celsius = float(input("Digite a temperatura em Celsius: "))
        kelvin = celsius_para_kelvin(celsius)
        print(f"{celsius}°C é igual a {kelvin:.2f}K")

    elif escolha == '4':
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        celsius = kelvin_para_celsius(kelvin)
        print(f"{kelvin}K é igual a {celsius:.2f}°C")

    elif escolha == '5':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        kelvin = fahrenheit_para_kelvin(fahrenheit)
        print(f"{fahrenheit}°F é igual a {kelvin:.2f}K")

    elif escolha == '6':
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        fahrenheit = kelvin_para_fahrenheit(kelvin)
        print(f"{kelvin}K é igual a {fahrenheit:.2f}°F")

    elif escolha == '7':
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")