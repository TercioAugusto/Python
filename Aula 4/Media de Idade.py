print("")
print("*"*25)
print("Media de Idade")
print("*"*25)
n=int(input("\nQuantos alunos tem na turma?\n"))
soma=0
for i in range(1,n+1):
    nome=input(f"Digite o nome do {i}° aluno:\n")
    idade=int(input(f"Digite a idade do {i}º aluno:\n"))
    soma+=idade
media=soma/n
print(f"A turma possui {n} alunos e a media de idades corresponde a {media:.2f}")    
