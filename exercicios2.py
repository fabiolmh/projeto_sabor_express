#Execicios (Módulos e funções)
#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
import os

#Função para seguir para o próximo programa:
def seguir():
    input('|====APERTE QUALQUER TECLA PARA SEGUIR. ====|')
    os.system('clear')

def par_impar(n):
    if n % 2 == 0:
        print('par')
    else:
        print('impar')

num = int(input('Informe um número: '))
os.system('clear')
print(f'O número {num} é:')
par_impar(num)
seguir()

os.system('clear')
#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.
def maior_menor(i):
    if 0 <= i <= 12:
        print('CRIANÇA')
    elif i <= 18:
        print('ADOLESCENTE')
    else:
        print('ADULTO')

idade = int(input('Informe sua idade: '))
maior_menor(idade)

seguir()

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
user = 'magaldapraia'
password = 'atecubanos'

login = input('Informe o usuário: ')
senha = input('Informe a senha: ')

os.system('clear')

if senha != password and login != user:
    print('CREDENCIAIS INVÁLIDAS')
elif senha != password:
    print('SENHA INVÁLIDA.')
elif login != user:
    print('USUÁRIO INVÁLIDO.')
else:
    print('LOGIN REALIZADO COM SUCESSO')
seguir()

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

x = int(input('Informe a coordenada para X: '))
y = int(input('Informe a coordenada para Y: '))

if x > 0 and y > 0:
    print('PRIMEIRO QUADRANTE.')
elif x < 0 and y > 0:
    print('SEGUNDO QUADRANTE.')
elif x < 0 and y < 0:
    print('TERCEIRO QUADRANTE.')
elif x > 0 and y < 0:
    print('QUARTO QUADRANTE.')
else:
    print('O PONTO ESTÁ LOCALIZADO NO EIXO OU ORIGEM.')

seguir()