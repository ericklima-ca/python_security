from threading import Thread
import time

def car(speed, pilot):
  path = 0
  while path <= 100:
    print(f'{pilot} - {path} km\n')
    path += speed
    time.sleep(0.2)

    
t_car_1 = Thread(target = car, args = [20, 'Pilot 1'])
t_car_2 = Thread(target = car, args = [30, 'Pilot 2'])

t_car_1.start()
t_car_2.start()
