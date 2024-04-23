import platform
import os
from mydb import search_on_db, create_on_db, edit_on_db, delete_on_db

def search_advogado():
    clean_screen()
    print('!!--> Busca de advogado <--!!')
    print('Escolha as opcoes:')
    print('[1] Busca via OAB')
    print('[2] Buscar Todos Advogados')
    print('[3] voltar')

    search = int(input('Digite a sua escolha: '))

    if search == 1:
        value = str(input('Digite a OAB: '))
        print(search_on_db(value))
        print('[1] - Buscar Novamente')
        print('[2] - Voltar')

        search = int(input('Digite sua opção: '))

        if search == 1:
            search_advogado()
        elif search == 2:
            main()
        else: 
            print('Opção inválida')
        
        
    elif search == 2:
        clean_screen()
        search_on_db('*')
        input('Pressione qualquer botão para voltar')
        main()

    elif search == 3:
        clean_screen()
        main()
    else:
        print('Opção inválida')

def create_advogado():
    clean_screen()
    print('Digite o nome completo do Advogado')
    name = str(input())
    print('Digite o endereço do advogado')
    address = str(input())
    print('Digite a OAB do advogado')
    oab = str(input())

    if len(oab) != 10:
        print('Valor de OAB errado!')

    print(create_on_db(name, address, oab))

def edit_advogado():
    clean_screen()
    print('Digite o valor da OAB para ser editada: ')
    oab = str(input())

    print('Escolha o campo para ser alterado:')
    print('[1] - Nome')
    print('[2] - Endereço')
    print('[3] - Oab')
    choose = int(input())

    print('Digite o novo valor!')

    new_value = str(input(''))
    edit_on_db(oab, choose, new_value)

    clean_screen()
    print('Alteração concluída:')
    print(search_on_db(oab))
    
    input('Pressione qualquer botão para voltar')

    main()

def delete_advogado():
    clean_screen()
    print('Digite o valor da OAB do advogado a ser editado: ')
    oab = str(input())
    print(search_on_db(oab))
    print('Gostaria de excluir esse advogado? [1] SIM || [2] NÃO')
    choose = int(input())
    
    if choose == 1:
        clean_screen()
        delete_on_db(oab)
    elif choose == 2:
        clean_screen()
        main()
        

def clean_screen():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def main():
    clean_screen()
    print('Bem vindo ao banco de dados da OAB')
    print('Escolha as opcoes:')
    print('[1] Busca de advogado')
    print('[2] Adicionar advogado')
    print('[3] Editar advogado')
    print('[4] Apagar advogado')

    entrada = int(input('Digite a sua escolha: '))

    if entrada == 1:
        search_advogado()
    elif entrada == 2:
        create_advogado()
    elif entrada == 3:
        edit_advogado()
    elif entrada == 4:
        delete_advogado()
main()