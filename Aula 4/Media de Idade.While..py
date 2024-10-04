print("")
print("*"*25)
print("Media de Idade com While")
print("*"*25)
continua="s"
somaidade=0
n=0
while (continua=="s" or continua=="S"):
    nome=input(f"Digite o nome do {n+1}º aluno: ")
    idade=int(input(f"Digite a idade do {n+1}º aluno: "))
    somaidade+=idade
    continua=input("Deseja continuar cadastrando? Digite (s) para sim ou (n) para não: ")
    if (continua=="s" or continua=="S" or continua=="n" or continua=="N"):
        n=n+1
    else:
        continua=input("Você digitou um número incorreto, para continuar cadastrando digite(s) para sim ou (n) para não: ")
print(f"Foram cadastrado {n} alunos")
mediaidade=somaidade/n
print(f"A média de idade da turma é {mediaidade:.2f}")
