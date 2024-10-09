def criar_lista():
    lista=[]
    continua="s"
    while continua.lower() == "s":
        item=int(input("Digite um item para adicionar a lista: "))
        lista.append(item)
        continua=input("Deseja continuar cadastrando? S para sim ou N para não: ")
    return lista
#Função para buscar um item na lista
def buscar_item(lista):
    item_buscado=int(input("Digite o item que voc}e deseja buscar na lista: "))
    if item_buscado in lista:
        print(f"O item {item_buscado} foi encontrado na lista.")
    else:
        print(f"O item {item_buscado} não está na lista.")
def main():
    print("Bem-vindo ao programa de criação de listas!")
    lista_usuario=criar_lista()
    print("Sua lista:",lista_usuario)
    buscar_item(lista_usuario)
main()
