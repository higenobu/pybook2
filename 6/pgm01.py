#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, pygame
from pygame import mixer
#pygameとmixerの初期化をします
pygame.init()
pygame.mixer.init()
#音楽サンプルをロードします（mp3形式の音楽を用意しておきます）

pygame.mixer.music.load('music1.wav')
#音楽をプレーします

pygame.mixer.music.play(10)

#画面のサイズ、動きの速度、色を設定
size = width, height = 500, 500
speed = [1, 1]
black = 0, 0, 0
#画面を設定
screen = pygame.display.set_mode(size)
#ハートの画像をロード
ht = pygame.image.load("happy.gif")
heart = ht.get_rect()

while 1:
    for h in pygame.event.get():
        if h.type == pygame.QUIT:
            pygame.mixer.music.fadeout(2000)
            sys.exit()
            

    heart = heart.move(speed)
    #ハートが四角の左右の枠に達したら方向を変える
    if heart.left < 0 or heart.right > width:
        speed[0] = -speed[0]
#ハートが四角の上下の枠に達したら方向を変える
    if heart.top < 0 or heart.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ht, heart)
    pygame.display.flip()
#10秒間の間隔をおく
    pygame.time.delay(10)    
