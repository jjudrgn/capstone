from gpiozero import MCP3208

adc = MCP3208(0)
print(adc.value)
