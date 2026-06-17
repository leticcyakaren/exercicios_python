alunos = []
print ("1 para cadastrar\n"'2 para remover\n'"3 para listar\n""0 para sair")

while True:

    menu = int(input("digite o que deseja fazer: "))

    if menu ==1:
        adicionar=input("digite o nome do aluno: ")
        alunos.append(adicionar)
    elif menu ==2:
        remover =input("digite o aluno que quer remover: ")  
        alunos.remove(remover)
        if remover in alunos:
            alunos.remove(remover)
        else:
            print("aluno nãao encontrado")    
    elif menu ==3:
        print (alunos)  

    elif menu ==0:
        break        

