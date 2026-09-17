# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string
valor_conta = float(input("digite o valor da conta"))
numero_pessoas = int(input("qual numero de pessoas"))
valor_final = int(input("qual o valor total da compra"))

print(f"o que cada um vai pagar:{valor_final :f:.2}")