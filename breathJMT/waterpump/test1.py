import RPi.GPIO as GPIO
import time

MOTER_A_A1=5
MOTER_A_B1=6
MOTER_B_A1=20
MOTER_B_B1=21

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTER_A_A1, GPIO.OUT)
GPIO.setup(MOTER_A_B1, GPIO.OUT)
#GPIO.setup(MOTER_B_A1, GPIO.OUT)
#GPIO.setup(MOTER_A_B1, GPIO.OUT)

MOTER_A_A1_PWM=GPIO.PWM(MOTER_A_A1, 20)
#MOTER_B_A1_PWM=GPIO.PWM(MOTER_B_A1, 20)
MOTER_A_A1_PWM.start(0)
#MOTER_B_A1_PWM.start(0)

GPIO.output(MOTER_A_B1,GPIO.LOW)
#GPIO.output(MOTER_B_B1,GPIO.LOW)

timer=10
while(timer):
    MOTER_A_A1_PWM.ChangeDutyCycle(50)
#    MOTER_B_A1_PWM.ChangeDutyCycle(50)
    time.sleep(1)
    timer= timer-1



