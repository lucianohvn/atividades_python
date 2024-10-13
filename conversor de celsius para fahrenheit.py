def celsius_para_fahrenheit(celsius):
    fahrenheit = (9 * celsius / 5) + 32
    return fahrenheit

try:
    temperatura_celsius = float(input("Digite a temperatura em °C: "))

    temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

    print(f"A temperatura em °F é: {temperatura_fahrenheit:.2f}°F")
except ValueError:
    print("Por favor, insira um valor válido.")