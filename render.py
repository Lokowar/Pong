import cores
import pygame  
import engine

def renderJogo(janela):

    SCORE_FONT = pygame.font.SysFont("times new roman", 50)

    # INICIAR PLACAR
    palheta1_placar = SCORE_FONT.render(f"{engine.PONTO_PALHETA1}", 1, cores.BRANCO)
    palheta2_placar = SCORE_FONT.render(f"{engine.PONTO_PALHETA2}", 1, cores.BRANCO)
    janela.blit(palheta1_placar, (400 // 4 - palheta1_placar.get_width() // 2, 20))
    janela.blit(palheta2_placar, (400 * (3/4) - palheta2_placar.get_width() // 2, 20))


    
