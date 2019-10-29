from gpiozero import MCP3208
import time


adc1 = MCP3208(0)
adc2 = MCP3208(1)

while(True):
    print(adc1.value)
    print('ADC1: {:.2f}'.format(adc1.value))
    print(adc2.value)
    print('ADC2: {:.2f}'.format(adc2.value)) 
    time.sleep(2)
