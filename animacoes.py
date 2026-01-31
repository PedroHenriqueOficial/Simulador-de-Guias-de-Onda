# ARQUIVO RESPONSÁVEL POR GERAR AS ANIMAÇÕES 2D

import matplotlib.pyplot as mp
import matplotlib.animation as ma
import constantes as cts
import calculos as calc

# VARIÁVEIS GLOBAIS INTERNAS PARA O LOOP DA ANIMAÇÃO

E_z, H_x, H_y = None, None, None

"""

    • Função que gera as animações 2D do projeto

"""

def animacao2D():
    
    global E_z, H_x, H_y
    
    # REINICIALIZA OS CAMPOS PARA COMEÇAR A ANIMAÇÃO DO ZERO
    
    E_z, H_x, H_y = calc.inicializarCampos()
    
    # CONFIGURAÇÃO DO TEMPO

    tempo_simulacao = 2.0 * cts.COMPRIMENTO_Z / cts.VELOCIDADE_LUZ_VACUO 
    
    # NA SEÇÃO B, AUMENTA-SE UM POUCO O TEMPO PARA VER A ONDA ESTACIONÁRIA OSCILAR
    
    if cts.LETRA == 'B':
        tempo_simulacao *= 2 
        
    passos = int(tempo_simulacao / cts.TEMPO)

    # CONFIGURAÇÃO DA FIGURA

    figura, ax = mp.subplots(figsize=(10, 4))
    im = ax.imshow(E_z, cmap = 'RdBu', vmin = -0.5, vmax = 0.5, origin = 'lower', extent = [0, cts.COMPRIMENTO_Z * 1000, 0, cts.A_LARGURA * 1000], animated = True)
    titulo = f"Propagação TE10 - {cts.FREQUENCIA_OPERACAO / 1e9:.2f} GHz"
    
    if cts.LETRA == 'B':
        titulo = f"Cavidade Ressonante - {cts.FREQUENCIA_OPERACAO / 1e9:.2f} GHz"

    ax.set_title(titulo)
    ax.set_xlabel("Comprimento Z (mm)")
    ax.set_ylabel("Largura X (mm)")
    cbar = mp.colorbar(im, ax = ax)
    cbar.set_label("Amplitude do Campo Elétrico (Ey)")

    tempo_texto = ax.text(0.02, 0.90, '', transform = ax.transAxes, color = 'black', bbox = dict(facecolor = 'white', alpha = 0.7))

    # FUNÇÃO DE ATUALIZAÇÃO INTERNA
    
    def atualizacao(frame):
    
        global E_z, H_x, H_y
    
        passos_frame = 5
        
        for _ in range(passos_frame):
            
            tempo = (frame * passos_frame + _) * cts.TEMPO
            
            H_x, H_y = calc.atualizarCampoMagnetico(E_z, H_x, H_y)
            E_z = calc.atualizarCampoEletrico(E_z, H_x, H_y)
            
            # A FONTE TOMA A DECISÃO DE QUAL USAR

            E_z = calc.fonte(E_z, tempo)
        
        im.set_array(E_z)
        tempo_atual_ps = frame * passos_frame * cts.TEMPO * 1e12
        tempo_texto.set_text(f"t = {tempo_atual_ps:.1f} ps")
        
        return im, tempo_texto

    # GERA A ANIMAÇÃO

    ani = ma.FuncAnimation(figura, atualizacao, frames = int(passos / 5), interval = 30, blit = True)
    mp.tight_layout()
    mp.show()
