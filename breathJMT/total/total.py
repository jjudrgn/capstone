from gpiozero import MCP3208
import time
import RPi.GPIO as GPIO
import Adafruit_DHT

#mcp setup
adc1 = MCP3208(0)
adc2 = MCP3208(1)

# water setup
MOTER_A_A1=5
MOTER_A_B1=6

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTER_A_A1, GPIO.OUT)
GPIO.setup(MOTER_A_B1, GPIO.OUT)

MOTER_A_A1_PWM=GPIO.PWM(MOTER_A_A1, 20)
MOTER_A_A1_PWM.start(0)
GPIO.output(MOTER_A_B1,GPIO.LOW)

#temp
sensor = Adafruit_DHT.DHT11

pin = 4

humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)


while(True):
    #print(adc1.value)
    print('water sensor ADC1: {:.2f}'.format(adc1.value))
    #print(adc2.value)
    print('light sensor ADC2: {:.2f}'.format(adc2.value))
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        #print(temperature)
        #print(humidity)
    else:
        print('Failed to get reading. Try again!')
    
    if adc1.value > 0.5: # water
        timer=5
        while(timer):
            print('water')
            MOTER_A_A1_PWM.ChangeDutyCycle(50)
            time.sleep(1)
            timer= timer-1
    MOTER_A_A1_PWM.ChangeDutyCycle(0)
    
    if temperature > 30: # fan
        print("do fan")
        
    if adc2.value > 0.4: # led
        print("LED ON")
        
    time.sleep(2)
    
    
    

