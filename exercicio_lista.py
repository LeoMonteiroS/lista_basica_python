import os

lista = []

while True:
    print('Selecionar uma opcao')
    print('-'*40)
    opcao = input('[1]Inserir [2]Apagar [3]Listar [4]Sair: ')
    print('-'*40)

    if opcao == '1':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == '2':
        os.system('cls') #apagando o terminal
        for indice, valor in enumerate(lista):
            print(indice, valor)
        indice_str = input('Digite o numero que vai apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError: #erro quando vc nao digita um numero inteiro
            print('Por favor digite um numero inteiro')
        except IndexError: #erro quando nao existe o item na lista
            print('Indice nao existe na lista')
        except Exception:
            print('Erro desconhecido')
    
    elif opcao == '3':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for indice, valor in enumerate(lista):
            print(indice, valor)

    elif opcao == '4':
        break

    else:
        print('Por favor, escolha uma opcao valida')