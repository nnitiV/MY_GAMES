import pygame as pg
from random import randint
pg.init()
x = 380     # max 530 min min 230 era 380
y = 100       #era 100
pos_x = 526
pos_y = 800
pos_y_a = 800
pos_y_c = 2500
timer = 0
tempo_segundo = 0

velocidade_outros = 12

velocidade = 10
fundo = pg.image.load('Imagens/fundo.png')
carro = pg.image.load('Imagens/carro.png')
formula = pg.image.load('Imagens/formula.png')
car_small = pg.transform.scale(carro, (100, 125))
formula_small = pg.transform.scale(formula, (100, 150))

font = pg.font.SysFont('arial black',30)
texto = font.render("Tempo: ",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

janela = pg.display.set_mode((800,600))
pg.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :
    pg.time.delay(50)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            janela_aberta = False

    comandos = pg.key.get_pressed()

    if comandos[pg.K_RIGHT] and x<= 520:
        x += velocidade
    if comandos[pg.K_LEFT] and x >= 230:
        x -= velocidade

    #           verifica a colisao
    if ((x + 80 > pos_x and y + 180 > pos_y) ):
        y = 1200

    if ((x - 80 < pos_x - 300 and y + 180 > pos_y_a)):
        y = 1200

    if ((x + 80 > pos_x - 136 and y + 180 > pos_y_c))and((x - 80 < pos_x - 136 and y + 180 > pos_y_c)):
        y = 1200

    if (pos_y <= -80):
        pos_y = randint(800,1000)

    if (pos_y_a <= -80):
        pos_y_a = randint(1200, 2000)

    if (pos_y_c <= -80):
        pos_y_c = randint(2200, 3000)

    if (timer <20):
        timer +=1
    else:
        tempo_segundo +=1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0

    pos_y  -= velocidade_outros
    pos_y_a -= velocidade_outros +2
    pos_y_c -= velocidade_outros +10    # carro preto


    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(formula, (pos_x, pos_y))
    janela.blit(formula, (pos_x - 300, pos_y_a))
    janela.blit(texto,pos_texto)
    pg.display.update()

pg.quit()
