#bibliotecas
import os
#variáveis globais:
restaurantes = []


#funçõesgerais

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

#Exibir subtítulo e limpando a tela
def exibir_subtitulo(texto):
	os.system('clear')
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

#Funções do fluxo do programa
#Exibir o menu de opções
def exibir_opcoes():
    print('1. CADASTRAR RESTAURANTE.')
    print('2. LISTAR RESTAURANTES.')
    print('3. ATIVAR RESTAURANTE.')
    print('4. SAIR.')

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
            alterar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            print('SAIR.')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

#Cadastrar restaurante
def cadastrar_restaurante():
    exibir_subtitulo('| CADASTRO DE RESTAURANTES |')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input('Qual a categoria do restaurante: ')
    ativo = False
    restaurantes.append({'nome': nome_do_restaurante, 'categoria' : categoria, 'ativo' : ativo})
    print(f'\n O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

#Listar restaurantes
def listar_restaurantes():
    exibir_subtitulo('|           LISTA DE RESTAURANTES              |')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativo' if restaurante['ativo'] else 'Desativado'
        print(f'- Nome do restaurante: {nome_restaurante} | Categoria: {categoria} | Situação no sistema: {ativo}.\n')
    voltar_ao_menu_principal()

#Ativar ou desativar restaurante
def alterar_estado_do_restaurante():
    exibir_subtitulo('|       ALTERNAR ESTADO DO RESTAURANTE       |')
    try:
        for i, restaurante in enumerate(restaurantes, start=1):    
            nome_restaurante = restaurante['nome']
            ativo = 'Ativo' if restaurante['ativo'] else 'Desativado'
            print(f'{i} - {nome_restaurante}') 
            print(f'Situação: {ativo} \n')      

        try:
            selecionar_restaurante = int(input('Escolha o restaurante que deseja alterar: '))
            restaurantes[selecionar_restaurante - 1]['ativo'] = not restaurantes[selecionar_restaurante -1]['ativo']
            print('Alterado com sucesso')
            main()
        except:
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
