print("*"*25)
print("Programa de Média")
print("*"*25)
nome=input("Digite o nome do aluno:\n")
nota1=float(input("Digite a nota da primeira avaliação do aluno:\n"))
nota2=float(input("Digite a nota da primeira avaliação do aluno:\n"))
media=(nota1+nota2)/2
if (media>=9):
    conc="A"
elif (media>=7.5):
    conc="B"
elif (media>=6):
    conc="C"
elif (media>=4):
    conc="D"
else:
    conc="E"
print(f"O aluno {nome} que teve {nota1} na primeira avaliação e {nota2} na segunda avaliação, ficou com a média {media:.1f} e conceito {conc}.")    
