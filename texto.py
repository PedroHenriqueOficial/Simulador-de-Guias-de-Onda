# ARQUIVO RESPONSÁVEL POR CONTER TODOS OS TEXTOS DO PROGRAMA

import constantes as cts

mensagemBoasVindas = f"""Seja bem vindo ao simulador eletromagnetico baseado no metodo das diferencas finitas no dominio do tempo (FDTD).

A simulacao representa um guia de onda retangular WR-10 de banda W.

O guia de onda possui as seguintes dimensoes: {cts.A_LARGURA * 1000:.2f} mm x {cts.B_ALTURA * 1000:.2f} mm.

O simulador possui grade de: {cts.NUMERO_PONTOS_X} x {cts.NUMERO_PONTOS_Z} células. """

mensagemMenu = """\nAbaixo tem-se as opcoes disponiveis:

    [A] Guia de Onda Retangular Comercial
    [B] Cavidade Ressonante Metalica
    [C] Antena de Guia de Onda com Fendas
    [D] Aplicacao Atual da Antena de Guia com Fendas 
"""

mensagemErro = "\nA opcao informada nao exite!"

mensagemA = """\nAbaixo tem-se as opcoes disponiveis:

    [A] Guia de Onda Retangular Comercial
        [1] Grafico Senoidal do Modo TE10
        [2] Simulacao 2D
    [B] Cavidade Ressonante Metalica
    [C] Antena de Guia de Onda com Fendas
    [D] Aplicacao Atual da Antena de Guia com Fendas
"""

mensagemB = """\nAbaixo tem-se as opcoes disponiveis:

    [A] Guia de Onda Retangular Comercial
    [B] Cavidade Ressonante Metalica
        [1] Grafico de Ressonancia
        [2] Simulacao 2D
    [C] Antena de Guia de Onda com Fendas
    [D] Aplicacao Atual da Antena de Guia com Fendas
"""

mensagemC = """\nAbaixo tem-se as opcoes disponiveis:

    [A] Guia de Onda Retangular Comercial
    [B] Cavidade Ressonante Metalica
    [C] Antena de Guia de Onda com Fendas
        [1] Grafico de Irradiacao da Antena
        [2] Simulacao 2D
    [D] Aplicacao Atual da Antena de Guia com Fendas
"""
