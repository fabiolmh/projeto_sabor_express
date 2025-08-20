#bibliotecas
import os
#variáveis globais:
restaurantes = []


#funções

#Exibir o nome do programa
def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

#Exibir o menu de opções
def exibir_opcoes():
    print('1. CADASTRAR RESTAURANTE.')
    print('2. LISTAR RESTAURANTES.')
    print('3. ATIVAR RESTAURANTE.')
    print('4. SAIR.')

#Exibir subtítulo e limpando a tela
def exibir_subtitulo(texto):
	os.system('clean')
	exibir_nome_do_programa()
	print(texto)
	print(' ')


#Voltar ao menu principal
def voltar_ao_menu_principal():
    input('Digite qualquer tecla para voltar para o menu principal')
    main()


#Exibir mensagem de opção inválida
def opcao_invalida():
    input('Opção inválida.')
    voltar_ao_menu_principal()

#Cadastrar restaurante
def cadastrar_restaurante():
    exibir_subtitulo('| CADASTRO DE RESTAURANTES |')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

#Listar restaurantes
def listar_restaurantes():
    exibir_subtitulo('|           LISTA DE RESTAURANTES              |')
    for i, restaurante in enumerate(restaurantes, start=1):
        print(f'{i}º- {restaurante}\n')
    voltar_ao_menu_principal()

#Escolher opção
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        os.system('clear')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes.')
        elif opcao_escolhida == 4:
            print('SAIR.')
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
#finalizando o app
def finalizando():
    exibir_subtitulo('APLICAÇÃO FINALIZADA.')


#code
def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    finalizando()

if __name__ == '__main__':
    main()
