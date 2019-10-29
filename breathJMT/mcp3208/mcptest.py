import spidev, time, os

spi = spidev.SpiDev()
spi.open(0,0)

def ReadAdc(chNum):
    if chNum > 7 or chNum < 0:
        return -1
    adc = spi.xfer2([1, (8 + chNum) << 4,0])
    adc_out = ((adc[1] & 3) << 8) + adc[2]
    return adc_out

def ConvertVolt(data, places):
    volt = ( data * 3.3) /float(1023)
    volt = round(volt, places)
    return volt

def ConvertTMP36(data, places):
    temp = ((data * 330) /float(1023)) -50
    temp = round(temp, places)
    return temp

delay =1

temp1_channel = 1
light1_channel = 0

while True:
    print"------------------------------------------------------"

 #   temp1_level = ReadAdc(temp1_channel)
 #   temp1_volt = ConvertVolt(temp1_level, 2)
 #   temp1 = ConvertTMP36(temp1_level, 2)
 #   print("TMP36 : Data {} ({}V) {} C".format(temp1_level, temp1_volt, temp1))

    light1_level = ReadAdc(light1_channel)
    light1_volt = ConvertVolt(light1_level, 2)
    print("Light1: Data {} ({}V)".format(light1_level, light1_volt))


    time.sleep(delay)


