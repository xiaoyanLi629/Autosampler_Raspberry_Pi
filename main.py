import time
from stepper_function import stepper_func

motor1 = [3, 5, 7, 8]
motor2 = [13, 11, 15, 12]
motor3 = [16, 18, 19, 21]
motor4 = [22, 23, 24, 26]

speed = 0.001
#motor1: x axis
#motor2: y axis
#motor3: z axis
#motor4: syringe
#syringe length 300
stepper_func(motor1, 2000, speed)
stepper_func(motor2, 800, speed)
stepper_func(motor3, -800, speed)
stepper_func(motor4, -800, speed)

for i in range(3):
    for j in range(5):
        stepper_func(motor1, (10000-j*200), speed)
        stepper_func(motor3, 500, speed)
        stepper_func(motor4, 300, speed)
        stepper_func(motor4, -300, speed)
        stepper_func(motor3, -500, speed)
        stepper_func(motor1, -(10000-j*200), speed)

        stepper_func(motor3, 400, speed)
        stepper_func(motor4, 300, speed)
        stepper_func(motor4, -300, speed)
        stepper_func(motor3, -400, speed)

        stepper_func(motor1, 200, speed)
    stepper_func(motor2, 200, speed)

