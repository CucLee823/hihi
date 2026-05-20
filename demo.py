import pygame
pygame.init()
#Tiêu đề và icon
p=0.2     #trọng lực
bird_y=0 #tọa độ con chim
score=0
game_play=True
h_score=0
game_font=pygame.font.Font(r"FileGame\04B_19.TTF",40)
def score_view():
    if game_play:
        score_f=game_font.render(f"Score: {str(int(score))}",True,(255,255,255))
        score_hcn=score_f.get_rect(center=(200,40))
        screen.blit(score_f,score_hcn)
    else :
        score_f = game_font.render(f"Score:{str(int(score))}", True, (255, 255, 255))
        score_hcn = score_f.get_rect(center=(200, 40))
        screen.blit(score_f, score_hcn)
        h_score_f = game_font.render(f"High Score:{str(int(h_score))}", True, (255, 255, 255))
        h_score_hcn = h_score_f.get_rect(center=(200, 100))
        screen.blit(h_score_f, h_score_hcn)
pygame.display.set_caption("Hửa Đen")

icon = pygame.image.load(r"FileGame\assets\yellowbird-downflap.png")
bg = pygame.image.load(r"FileGame\assets\background-night.png")
fl = pygame.image.load(r"FileGame\assets\floor.png")
bg=pygame.transform.scale2x(bg)
pygame.display.set_icon(icon)
fl_x=0
#cửa sổ game
screen=pygame.display.set_mode((400,670))
#Đưa bird
bird1 = pygame.image.load(r"FileGame\assets\yellowbird-midflap.png")
bird1=pygame.transform.scale2x(bird1)
bird_hcn=bird1.get_rect(center=(100,350))
#Màn game over
screenover = pygame.image.load(r"FileGame\assets\message.png")
screenover=pygame.transform.scale2x(screenover)
screenover_hcn=bird1.get_rect(center=(100,250))
#Hàm check va chạm
def check_vc():
    if bird_hcn.bottom >= 570 or bird_hcn.top <=-75:
       return  False
    else: return True
#vòng lặp xử l game
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and game_play:
                bird_y=-10
            if event.key == pygame.K_RIGHT and game_play==False:
                game_play=True
                bird_y=0
                bird_hcn.center=(60,100)
                score=0
    screen.blit(bg,(0,0))
    fl_x -= 1
    screen.blit(fl,(fl_x,550))
    screen.blit(fl, (fl_x+335, 550))
    if fl_x==-335:
        fl_x=0
    if game_play:
    #đưa bird vào
        screen.blit(bird1,(bird_hcn))
        bird_y+=p
        bird_hcn.centery+=bird_y
        score+=0.01
        if score>h_score:h_score=score
        score_view()
        game_play=check_vc()
    else :
        screen.blit(screenover,(screenover_hcn))
        score_view()
    pygame.display.update()