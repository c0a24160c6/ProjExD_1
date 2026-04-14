import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習1
    rbg_img = pg.transform.flip(bg_img, True,False)
    kot_img = pg.image.load("fig/3.png") #練習3
    kot_img = pg.transform.flip(kot_img, True , False)
    kot_rct = kot_img.get_rect() #こうかとんのrect属性
    kot_rct.center = 300,200 #初期座標
    screen.blit(kot_img,kot_rct)
    
    tmr = 0

    while True:
    
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        x = 0
        y = 0
        if key_lst[pg.K_UP] :
            y -= 1
        if key_lst[pg.K_DOWN] :
            y += 1
        if key_lst[pg.K_LEFT] :
            x -= 1
        if key_lst[pg.K_RIGHT] :
            x += 1
        else: #風の実装
            x -= 1
        kot_rct.move_ip((x , y))
        x = tmr%3200 #練習6
        screen.blit(bg_img, [-x, 0]) #練習2
        screen.blit(rbg_img, [-x+1600, 0]) #練習7 
        screen.blit(rbg_img, [-x+3200, 0]) #練習8
        screen.blit(kot_img, kot_rct) #練習4
        
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()