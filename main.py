# ARQUIVO PRINCIPAL RESPONSÁVEL POR UNIR TODOS OS ARQUIVOS

import constantes as cts
import calculos as calc

from menu import menu
from graficos import graficoSenoide, graficoRessonancia, graficoDiagramaIrradiacao
from animacoes import animacao2D

# EXIBIÇÃO DO MENU

menu()

# CONTROLE DE FLUXO

match cts.LETRA:

    case 'A': 
        
        match cts.NUMERO:
            
            case 1:
                
                E_z, H_x, H_y = calc.inicializarCampos()
                
                for i in range(1500): 
                
                    t = i * cts.TEMPO
                    H_x, H_y = calc.atualizarCampoMagnetico(E_z, H_x, H_y)
                    E_z = calc.atualizarCampoEletrico(E_z, H_x, H_y)
                    E_z = calc.fonte(E_z, t)
                
                graficoSenoide(E_z)
                
            case 2:
                animacao2D()

    case 'B': 
        
        match cts.NUMERO:
        
            case 1:
                graficoRessonancia()
        
            case 2:
                animacao2D()

    case 'C':

        match cts.NUMERO:

            case 1:
                graficoDiagramaIrradiacao()

            case 2:
                animacao2D()
