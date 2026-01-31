# ARQUIVO QUE GUARDA AS FUNÇÕES RESPONSÁVEIS DE FAZER OS CÁLCULOS

import numpy as np
import constantes as cts

"""_________________________________________________________________ SEÇÃO A _________________________________________________________________"""

"""

    • Cria as matrizes de zero para os campos.
    • E_z define o campo elétrico transversal (E_y do guia real).
    • H_x e H_y (no gráfico) representam os campos magnéticos H_x e H_z do guia real.

"""

def inicializarCampos():

    E_z = np.zeros((cts.NUMERO_PONTOS_X, cts.NUMERO_PONTOS_Z))
    H_x = np.zeros((cts.NUMERO_PONTOS_X, cts.NUMERO_PONTOS_Z)) 
    H_y =np.zeros((cts.NUMERO_PONTOS_X, cts.NUMERO_PONTOS_Z))

    return E_z, H_x, H_y

"""

    • Atualiza o campo magnético baseado no rotacional do campo elétrico.
    • Equações discretizadas no tempo e espaço
    • Update de H_x aqui representado pela dimensão z do gráfico
    • Update de H_y aqui representado pela dimensão x do gráfico

"""

def atualizarCampoMagnetico(E_z, H_x, H_y):
    
    multiplicador = cts.TEMPO / (cts.PERMEABILIDADE_MAGNETICA * cts.DIMENSAO_X)
    H_x[:, :-1] -= multiplicador * (E_z[:, 1:] - E_z[:, :-1])
    H_y[:-1, :] += multiplicador * (E_z[1:, :] - E_z[:-1, :])

    return H_x, H_y

"""

    • Atualiza o campo elétrico baseado no rotacional do campo magnético.
    • Equações discretizadas no tempo e espaço

"""

def atualizarCampoEletrico(E_z, H_x, H_y):
    
    multiplicador = cts.TEMPO / (cts.PERMESSIVIDADE_ELETRICA * cts.DIMENSAO_X)

    E_z[1:-1, 1:-1] += multiplicador * ((H_y[1:-1, 1:-1] - H_y[:-2, 1:-1]) - (H_x[1:-1, 1:-1] - H_x[1:-1, :-2]))

    return E_z

"""

    • Calcula a largura temporal do pulso

"""

def larguraTemporalPulsoA(tempo, frequencia):

    largura_temporal_pulso = 1.0 / (0.3 * frequencia)
    tempo_inicial = 3 * largura_temporal_pulso
    resultado = np.exp(-((tempo - tempo_inicial) / largura_temporal_pulso)**2) * np.sin(2 * np.pi * frequencia * tempo)

    return resultado

"""

    • Aplica a fonte no gráfico forçando o campo elétrico
    • A fonte tem o perfil espacial do modo TE10
    • Coloca a fonte na posição Z definida

"""

def fonte(E_z, tempo):

    coordenada_X = np.arange(cts.NUMERO_PONTOS_X) * cts.DIMENSAO_X
    espaco = np.sin(np.pi * coordenada_X / cts.A_LARGURA)
    valor_tempo_atual = larguraTemporalPulsoA(tempo, cts.FREQUENCIA_OPERACAO)
    E_z[:, cts.POSICAO_FONTE_EIXO_Z] += valor_tempo_atual * espaco

    return E_z

"""_________________________________________________________________ SEÇÃO B _________________________________________________________________"""

"""

    • Gera um pulso curto (20 picosegundos)
    • Usado para excitar todas as frequências da cavidade e achar ressonâncias.

"""

def pulsoCurto(tempo):

    largura_Pulso = 20e-12
    centro_pulso = 4 * largura_Pulso

    return np.exp(-((tempo - centro_pulso) / largura_Pulso)**2)

"""
   
    • Aplica a fonte no campo.
    • Fonte senoidal pura e contínua
    • A aplicação 'se soma' para não zerar ondas refletidas.
    • Excita vários modos, não só o TE10

"""

def larguraTemporalPulsoB(tempo, frequencia):

    periodo = 1.0 / frequencia

    return (tempo / (5 * periodo)) * np.sin(2 * np.pi * frequencia * tempo) if tempo < 5 * periodo else np.sin(2 * np.pi * frequencia * tempo)

"""

    • Fonte exclusiva para o gráfico de FFT
    • Usa apenas o pulso curto

"""

def fonteRessonancia(E_z, tempo):
   
    valor = pulsoCurto(tempo)
    centro_x = int(cts.NUMERO_PONTOS_X / 2)
    coordenada_z = 5 
    E_z[centro_x, coordenada_z] += valor
    
    return E_z

"""_______________________________________________________________ SEÇÃO A e B _______________________________________________________________"""

"""

    • Fonte para as animações 2D
    • Verifica em qual seção estamos - A ou B - e escolhe o pulso correto

"""

def fonte(E_z, tempo):
    
    coordenada_X = np.arange(cts.NUMERO_PONTOS_X) * cts.DIMENSAO_X
    espaco = np.sin(np.pi * coordenada_X / cts.A_LARGURA)
    
    # DECIDE EM QUAL SEÇÃO ESTAMOS - A OU B

    if cts.LETRA == 'A':
        valor_tempo = larguraTemporalPulsoA(tempo, cts.FREQUENCIA_OPERACAO)
    
    else: 
        valor_tempo = larguraTemporalPulsoB(tempo, cts.FREQUENCIA_OPERACAO)

    E_z[:, cts.POSICAO_FONTE_EIXO_Z] += valor_tempo * espaco
    
    return E_z
