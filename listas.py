#Crie um programa que permita ao usuário cadastrar frutas em uma lista até que ele digite uma palavra
#para encerrar o cadastro. Ao final, exiba todas as frutas cadastradas.

frutas=[]

while True:

    adicionar = input("digite qual fruta deseja adicionar(digite fim para sair): ")
 

    if adicionar == "fim":
    
        break
    else:
        frutas.append(adicionar)
print(frutas)

#Cadastre 5 nomes de convidados em uma lista e depois exiba a lista completa e a quantidade de convidados.

convidados = []
contador = 5

while contador >0:
    lista=input("adicione o nome do convidado: ")
    convidados.append(lista)
    contador=contador-1


print("\nLista de convidados:")
print(convidados)

print("\nQuantidade de convidados:")
print(len(convidados))
