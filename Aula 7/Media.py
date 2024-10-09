continua="s"
idade=[]
while (continua == "s" or continua == "S"):
    id = int(input(f"Digite a idade do aluno: "))
    idade.append(id)
    continua = input(f"Deseja continua cadastrando? S para sim N para não: ")
soma_idade=0
n=len(idade)
for i in range(n):
    soma_idade+=idade[i]
media_idade=soma_idade/n
print(f"Está turma possui {n} alunos e a media de idade é: {media_idade}")
qmaior=qmenor=0
for i in range(n):
    if idade[i] >=18:
        qmaior = qmaior +1
    else:
        qmenor = qmenor +1
print(f"Na turma temos {qmaior} alunos maiores de idade e {qmenor} alunos menores de idade")
