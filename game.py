import pygame
from population import Population
from globals import MAX_WIDTH, MAX_HEIGHT

pygame.init()
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
clock = pygame.time.Clock()
running = True

position_x = 1
position_y = 1

# POPULATION
population = Population(100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.key.key_code("1"):
                print("Deleting population")
                population.delete_left_half()
                # population.delete_popualtion()
            if event.key == pygame.key.key_code("C"):
                print("Creating new population")
                population = Population(100)
            if event.key == pygame.key.key_code("D"):
                print("Inheriting new population")
                


    screen.fill("gray")

    for person in population.people:
        position = pygame.Rect(person.position_x, person.position_y, person.width, person.height)
        pygame.draw.ellipse(screen, "red", position)
        person.do_action()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()