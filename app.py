#bibliotecas
import os

#funções
def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
    print('1. CADASTRAR RESTAURANTE.')
    print('2. LISTAR RESTAURANTES.')
    print('3. ATIVAR RESTAURANTE.')
    print('4. SAIR.')

def opcao_invalida():
    input('Opção inválida. Digite qualquer tecla para voltar.')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        os.system('clear')

        if opcao_escolhida == 1:
            print('Cadastrar restaurante.')
        elif opcao_escolhida == 2:
            print('Listar restaurantes.')
        elif opcao_escolhida == 3:
            print('Ativar restaurantes.')
        elif opcao_escolhida == 4:
            print('SAIR.')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizando():
    print('finalizando o app...')
#code
def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    finalizando()

if __name__ == '__main__':
    main()