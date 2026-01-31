# ARQUIVO RESPONSÁVEL PELA CRIAÇÃO DO MENU

import constantes as cts
import texto as txt

from os import system, name

"""

    • Função responsável por limpar a tela do programa. 

"""

def limparTela():

    system('cls' if name == 'nt' else 'clear')

"""

    • Função responsável por criar o menu.
    • Dentro desta função define-se algumas constantes do arquivo chamado 'constantes.py'.

"""

def menu():

    limparTela()

    print(txt.mensagemBoasVindas)
    print(txt.mensagemMenu)
    
    letra = input("Informe a letra escolhida: ").strip().upper()[:1]

    while (letra != 'A' and letra != 'B' and letra != 'C' and letra != 'D'):

        limparTela()

        print(txt.mensagemErro)
        print(txt.mensagemMenu)

        letra = input("Informe a letra escolhida: ").strip().upper()[:1]

    match letra:

        case 'A':
            
            cts.FREQUENCIA_OPERACAO = 90e9
            cts.LETRA = 'A'

            limparTela()

            print(txt.mensagemA)

            numero = int(input("Informe o numero escolhido: "))

            while (numero != 1 and numero != 2):

                limparTela()

                print(txt.mensagemErro)
                print(txt.mensagemA)

                numero = int(input("Informe o numero escolhido: "))

            match numero:

                case 1:
                    cts.NUMERO = 1
                case 2:
                    cts.NUMERO = 2
        
        case 'B':
            
            cts.FREQUENCIA_OPERACAO = 85.0e9
            cts.LETRA = 'B'

            limparTela()

            print(txt.mensagemB)

            numero = int(input("Informe o numero escolhido: "))

            while (numero != 1 and numero != 2):

                limparTela()

                print(txt.mensagemErro)
                print(txt.mensagemB)

                numero = int(input("Informe o numero escolhido: "))

            match numero:

                case 1:
                    cts.NUMERO = 1
                case 2:
                    cts.NUMERO = 2

        case 'C':

            cts.FREQUENCIA_OPERACAO = 90e9
            cts.LETRA = 'C'

            limparTela()

            print(txt.mensagemC)

            numero = int(input("Informe o numero escolhido: "))

            while (numero != 1 and numero != 2):

                limparTela()

                print(txt.mensagemErro)
                print(txt.mensagemC)

                numero = int(input("Informe o numero escolhido: "))

            match numero:

                case 1:
                    cts.NUMERO = 1
                case 2:
                    cts.NUMERO = 2
