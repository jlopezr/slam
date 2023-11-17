import env
import sensors
import pygame
import math

environment = env.buildEnvironment((600, 1200))
environment.originalMap = environment.map.copy()
lasers = sensors.LaserSensor(200, environment.originalMap, uncertainty=(0.5, 0.01))
environment.map.fill((0,0,0))
environment.infomap = environment.map.copy()
running = True

while running:
    sensorON = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False
    if sensorON:
          position = pygame.mouse.get_pos()
          lasers.position = position
          sensor_data = lasers.sense_obstacles()
          if not sensor_data is False:
            environment.dataStorage(sensor_data)
            environment.show_sensorData()

    environment.map.blit(environment.infomap, (0, 0))             
    pygame.display.update()