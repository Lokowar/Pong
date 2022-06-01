import objetos

def checarColisao(bola, palheta1, palheta2):
    # QUICAR BOLA
    if bola.y + bola.raio >= 300:
        bola.y_vel *= -1
    elif bola.y - bola.raio <= 0:
        bola.y_vel *= -1

    if bola.x_vel < 0:
        if bola.y >= palheta1.y and bola.y <= palheta1.y + palheta1.altura:
            if bola.x - bola.raio <= palheta1.x + palheta1.largura:
                bola.x_vel *= -1

                # DETECTA A PARTE CENTRAL DA PALHETA
                mid_y = palheta1.y + palheta1.altura / 2


                diferença_y = mid_y - bola.y
                fator_redução = (palheta1.altura / 2) / bola.MAX_VEL
                bola.y_vel = diferença_y / fator_redução   

                bola.y_vel = -1 * bola.y_vel

    else:
        if bola.y >= palheta2.y and bola.y <= palheta2.y + palheta2.altura:
            if bola.x - bola.raio >= palheta2.x:
                bola.x_vel *= -1

                # DETECTA A PARTE CENTRAL DA PALHETA
                mid_y = palheta2.y + palheta2.altura / 2
                
                difença_y = mid_y - bola.y
                fator_redução = (palheta2.altura / 2) / bola.MAX_VEL
                bola.y_vel = difença_y / fator_redução    

                bola.y_vel = -1 * bola.y_vel
