import math

num = int(input("Digite um número inteiro para calcular o fatorial: "))
if num < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
else:
    fatorial = math.factorial(num)
    print(f"O fatorial de {num} é: {fatorial}")