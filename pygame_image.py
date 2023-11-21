import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") #1
    m_bg_img = pg.transform.flip(bg_img,True,False)
    tori_img = pg.image.load("ex01/fig/3.png")
    tori_img = pg.transform.flip(tori_img,True,False)#2
    tori_list = [tori_img,pg.transform.rotozoom(tori_img,10,1.0)]*50#3
    tmr = 0
    i = 0
    y = 100
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -(tmr%3200)
        if ((tmr//100)%2==0):
            i = -10
        elif((tmr//100)%2==1):
            i = +10
        screen.blit(bg_img, [x, 0])#4
        screen.blit(m_bg_img, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(tori_list[tmr//100],[300,200+i])#5
        
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()