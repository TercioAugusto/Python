print("*"*25)
print("Programa de Cálculo Salarial")
print("*"*25)
nome=input("Digite o nome do funcionário\n")
salario=float(input("Digite o salário do funcionário\nR$ "))
tempo=int(input("Digite o tempo de empresa do funcionário\n"))
if tempo<5:
    novo_sal=salario+salario*0.06
elif tempo<10:
    novo_sal=salario+salario*0.10
elif tempo<15:
    novo_sal=salario+salario*0.15
else:
    novo_sal=salario+salario*0.20
print(f"O salário recalculado do funcionario {nome} corresponde á R${novo_sal:.2f}.")
