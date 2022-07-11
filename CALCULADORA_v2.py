print("=============================")
print("CALCULADORA 2.0")
print("=============================")

operacao = input("Selecione a operação desejada (somar, subtrair, multiplicar, dividir ou potenciação): ")
numero1 = input("Insira o primeiro número da operação: ")
numero2 = input("Insira o segundo número da operação - em caso de potenciação, o número ao qual o primeiro será elevado: ")

if operacao == "somar":
    resultado = float(numero1) + float(numero2)
elif operacao == "subtrair":
    resultado = float(numero1) - float(numero2)
elif operacao == "multiplicar":
    resultado = float(numero1) * float(numero2)
elif operacao == "dividir":
    resultado = float(numero1) / float(numero2)
elif operacao == "potenciação":
    resultado = float(numero1) ** float(numero2)
else:
    resultado = "Operação não suportada, utilizar 'somar, subtrair, multiplicar, dividir ou potenciação'."

print("O resultado da operação é: " + str(resultado))
