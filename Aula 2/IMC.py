print("******************************")
print("Calculadora de IMC")
print("******************************")
print("\n")
nome= input("Digite o seu nome: ")
idade=int(input("Digite a sua idade: "))
altura=float(input("Digite a sua altura (em metros): "))
peso=float(input("Digite o seu peso (em kg): "))
imc=peso/(altura**2)
if (imc<18.5):
    classificacao="Abaixo do Peso"
elif (imc<24.9):
    classificacao="Peso normal"
elif (imc<29.9):
    classificacao="Sobrepeso"
elif (imc<34.9):
    classificacao="Obesidade grau 1"
elif (imc<39.9):
    classificacao="Obesidade grau 2"
else:
    classificacao="Obesidade grau 3"
print(f"\nNome: {nome}")
print(f"\nIdade: {idade} anos")
print(f"\nAltura: {altura:.2f}m")
print(f"\nPeso: {peso}kg")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
