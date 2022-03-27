import pygame as pg
from random import randint as rd
pg.init()

x = 380
y = 50
pos_x = 526
pos_y = 800
pos_y_a = 800
pos_y_c = 800

velocidade = 15
velocidade_f = 12

fundo = pg.image.load('Imagens/fundo.png')
carro = pg.image.load('Imagens/carro.png')
formula = pg.image.load('Imagens/formula.png')
car_small = pg.transform.scale(carro, (100, 125))
formula_small = pg.transform.scale(formula, (100, 150))

font = pg.font.SysFont("arial black", 20)
texto = font.render('Tempo: ', True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (55, 40)
timer = 0
tempo_segundo = 0

janela = pg.display.set_mode((800, 600))
pg.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta:
    pg.time.delay(50)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            janela_aberta = False

    comandos = pg.key.get_pressed()

    if comandos[pg.K_s] and y <= 475:
        y += velocidade
    if comandos[pg.K_w] and y >= -5:
        y -= velocidade
    if comandos[pg.K_d] and x <= 625:
        x += velocidade
    if comandos[pg.K_a] and x >= 107.5:
        x -= velocidade
    if comandos[pg.K_r]:
        y = 50
        x = 380

    if(x + 50 > pos_x and y + 120 > pos_y + 10) and (x - 60 < pos_x and y - 120 < pos_y):
        y = 1200
    if ((x - 125 < pos_x - 420 and y + 120 > pos_y_a + 10)) and (x - 120 > pos_x - 520 and y + 50 < pos_y_a + 180 ):
        y = 1200
    if ((x + 50 > pos_x - 150 and y + 120 > pos_y_c + 10)) and (x + 50 < pos_x - 50 and y + 120 < pos_y_c + 240):
        y = 1200

    if ((pos_y <= -180)):
        pos_y = rd(800, 1000)
    if ((pos_y_a <= -180)):
        pos_y_a = rd(1300, 2000)
    if ((pos_y_c <= -180)):
        pos_y_c = rd(2300, 3000)

    if(timer < 15):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render('Tempo: '+str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0

    pos_y -= velocidade_f
    pos_y_a -= velocidade_f + 6
    pos_y_c -= velocidade_f + 12

    janela.blit(fundo, (0, 0))
    janela.blit(car_small, (x, y))
    janela.blit(formula_small, (pos_x, pos_y))
    janela.blit(formula_small, (pos_x - 350, pos_y_a))
    janela.blit(formula_small, (pos_x - 150, pos_y_c))
    janela.blit(texto, pos_texto)
    pg.display.update()

pg.quit()
