# ARQUIVO RESPONSÁVEL POR MOSTRAR OS GRÁFICOS

import numpy as np
import matplotlib.pyplot as plt
import constantes as cts
import calculos as calc

"""_________________________________________________________________ SEÇÃO A _________________________________________________________________"""

"""

    • Mostra um gráfico para visualizar a senoide do modo TE10.

"""

def graficoSenoide(E_z):
    
    centro_x = int(cts.NUMERO_PONTOS_X / 2)
    corte = E_z[centro_x, :]

    # CRIA O GRÁFICO DA SENOIDE

    plt.figure(figsize=(10, 4))
    plt.plot(np.linspace(0, cts.COMPRIMENTO_Z * 1000, cts.NUMERO_PONTOS_Z), corte, color = 'black')
    plt.title("Corte Longitudinal (Centro)")
    plt.xlabel("Comprimento Z (mm)")
    plt.ylabel("Amplitude do Campo")
    plt.grid(True)
    plt.show()

"""_________________________________________________________________ SEÇÃO B _________________________________________________________________"""

"""

    • Mostra um gráfico para visualizar os modos ressonântes.
    • Cada pico do gráfico representa uma frequência de ressonância de um modo TE específico.

"""

def graficoRessonancia():

    E_z, H_x, H_y = calc.inicializarCampos()

    sinal = [] # LISTA QUE GUARDA O SINAL MEDIDO AO LONGO DO TEMPO (PARA FAZER A FFT DEPOIS)

    # PONTO ESCOLHIDO ALEATORIAMENTE PARA PEGAR VÁRIOS MODOS

    ponto_X = int(cts.NUMERO_PONTOS_X * 0.5)
    ponto_Z = int(cts.NUMERO_PONTOS_Z * 0.75)

    # AUMENTA O TEMPO DE SIMULAÇÃO PARA PERMITIR QUE A RESSONÂNCIA SE ESTABILIZE
    
    pontos_extras = 4000 
    pontos_totais = int(2.0 * cts.COMPRIMENTO_Z / cts.VELOCIDADE_LUZ_VACUO / cts.TEMPO) + pontos_extras

    for i in range(pontos_totais):
        
        tempo = i * cts.TEMPO
        
        # ATUALIZA OS CAMPOS

        H_x, H_y = calc.atualizarCampoMagnetico(E_z, H_x, H_y)
        E_z = calc.atualizarCampoEletrico(E_z, H_x, H_y)
        
        # APLICA A FONTE NOS PRIMEIROS 100 PICOSEGUNDOS E, DEPOIS DE UM TEMPO, PARAMOS A FONTE E DEIXAMOS A CAVIDADE IR SOZINHA
        
        if tempo < 100e-12:
            
            E_z = calc.fonteRessonancia(E_z, tempo)
            
        # GRAVA O VALOR DO CAMPO NA SONDA
        
        sinal.append(E_z[ponto_X, ponto_Z])

    # ANÁLISE DE FREQUÊNCIA (FFT)
    
    sinal = np.array(sinal)
    dt = cts.TEMPO
    numero = len(sinal)

    # CÁLCULO DA FFT

    frequencias = np.fft.rfftfreq(numero, d = dt)
    amplitudes = np.abs(np.fft.rfft(sinal))

    # GRÁFICO DE RESSONÂNCIA

    plt.figure(figsize=(10, 6))
    plt.plot(frequencias / 1e9, amplitudes, color = 'darkblue')
    plt.title("Frequências de Ressonância da Cavidade WR-10 (L=15mm)")
    plt.xlabel("Frequência (GHz)")
    plt.ylabel("Amplitude da Resposta")
    plt.xlim(0, 150) # MOSTRA ATÉ 150 GHz
    plt.grid(True)
    plt.axvline(x = cts.FREQUENCIA_OPERACAO/1e9, color = 'red', linestyle = '--', label =f'{cts.FREQUENCIA_OPERACAO} GHz')
    plt.legend()
    plt.show()

"""_________________________________________________________________ SEÇÃO C _________________________________________________________________"""

"""

    • Mostra um gráfico para visualizar o diagrama de irradiação da antena.

"""

def graficoDiagramaIrradiacao():
    
    E_z, H_x, H_y = calc.inicializarCamposAntena()
    
    # TEMPO DE SIMULAÇÃO
    
    passos = 1500 
    
    # GUARDA A INTENSIDADE NO TOPO
    
    intensidade_topo = np.zeros(cts.NUMERO_PONTOS_Z)
    
    for i in range(passos):
        
        tempo = i * cts.TEMPO
        
        H_x, H_y = calc.atualizarCampoMagnetico(E_z, H_x, H_y)
        E_z = calc.atualizarCampoEletrico(E_z, H_x, H_y)
        
        # APLICA AS PAREDES E FENDAS
        
        E_z = calc.aplicarCondicoesAntena(E_z)
        
        # FONTE
        
        E_z = calc.fonteAntena(E_z, tempo)
        
        # ACUMULA ENERGIA NO TOPO DO DOMÍNIO

        intensidade_topo += E_z[-5, :]**2

    valor_maximo = np.max(intensidade_topo)
    
    # TRATAMENTO DE ERRO CASO DER DIVISÃO POR ZERO

    if valor_maximo > 0:
        intensidade_topo = intensidade_topo / valor_maximo
    
    else:
        print("Nenhuma energia detectada no topo. Verifique se as fendas estão abertas.")
   
    # PLOTAGEM
   
    coordenada_Z = np.arange(cts.NUMERO_PONTOS_Z)
    
    plt.figure(figsize=(10, 5))
    plt.plot(coordenada_Z, intensidade_topo, color = 'red', linewidth = 2, label = "Padrão de Irradiação")
    plt.title("Padrão de Irradiação (Intensidade no Campo Distante)")
    plt.xlabel("Posição Z (índices)")
    plt.ylabel("Potência Normalizada")
    plt.grid(True)
    plt.fill_between(coordenada_Z, intensidade_topo, color = 'red', alpha = 0.3)
    
    # DESENHA LINHAS ONDE DEVERIAM ESTAR AS FENDAS

    for f in range(cts.NUMERO_FENDAS):
        
        z_idx = int((cts.POSICAO_PRIMEIRA_FENDA + f * cts.ESPACAMENTO_FENDAS) / cts.DIMENSAO_Z)
        
        if f == 0:
            plt.axvline(x = z_idx, color = 'black', linestyle = '--', alpha = 0.5, label = "Posição das Fendas")
        
        else:
            plt.axvline(x = z_idx, color = 'black', linestyle = '--', alpha = 0.5)
    
    plt.legend()
    plt.show()
