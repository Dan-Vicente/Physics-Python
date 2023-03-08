import pygame
import math

pygame.init()

# Definindo as dimensões da janela
screen_width = 800
screen_height = 600

# Definindo as cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Definindo as posições e cargas das partículas
particle1_pos = [200, 300]
particle1_charge = 1
particle2_pos = [600, 300]
particle2_charge = -1

# Criando a janela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Linhas de Campo Elétrico")

# Função para calcular o campo elétrico em um ponto
def electric_field(x, y, particle_pos, particle_charge):
    dx = particle_pos[0] - x
    dy = particle_pos[1] - y
    r = math.sqrt(dx**2 + dy**2)
    if r == 0:
        return (0, 0)
    else:
        k = 9e9 # constante eletrostática
        e = k * particle_charge / r**2
        ex = e * dx / r
        ey = e * dy / r
        return (ex, ey)

# Função para desenhar as linhas de campo elétrico
def draw_field_lines():
    step = 20
    for x in range(0, screen_width, step):
        for y in range(0, screen_height, step):
            e1 = electric_field(x, y, particle1_pos, particle1_charge)
            e2 = electric_field(x, y, particle2_pos, particle2_charge)
            ex = e1[0] + e2[0]
            ey = e1[1] + e2[1]
            mag = math.sqrt(ex**2 + ey**2)
            if mag > 0:
                ex = ex / mag
                ey = ey / mag
                pygame.draw.line(screen, red, [x, y], [x + ex*step, y + ey*step])

# Loop principal
running = True
while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pintando o fundo
    screen.fill(white)

    # Desenhando as partículas
    pygame.draw.circle(screen, black, particle1_pos, 20)
    pygame.draw.circle(screen, black, particle2_pos, 20)

    # Desenhando as linhas de campo elétrico
    draw_field_lines()
    #dra
    particle1_vel = [0, 0]
    particle2_vel = [0, 0]
    particle1_pos[0] += particle1_vel[0]
    particle1_pos[1] += particle1_vel[1]

    particle2_pos[0] += particle2_vel[0]
    particle2_pos[1] += particle2_vel[1]
   

    # Atualizando a janela
    pygame.display.update()

# Saindo do pygame
pygame.quit()
