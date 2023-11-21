import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") #1
    tori_img = pg.image.load("ex01/fig/3.png")
    tori_img = pg.transform.flip(tori_img,True,False)#2
    tori_img = pg.transform.rotozoom(tori_img,10,1.0)#3
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])#4
        screen.blit(tori_img,[0,0])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()