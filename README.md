## Sensors
- Temperature - DS18B20, 1-Wire: https://sizable.se/P.29Z3D/DS18B20-Temperatursensor-vattentat-med-1-meter-kabel 
- Mositure - Capacative moisture sensor v.1.2 -> Analog output -> **! Requries ADC -> digital converter... !**
- Analog to digital converter: https://sizable.se/P.7PWUQ/ADS1015-ADC-4-kanaler-12bit-I2C-16x-programmerbar-forstarkning


### Temperature
sudo modprobe w1_therm
sudo modprobe w1_gpio

Add 'dtoverlay=w1-gpio,gpiopin=23' in /boot/config.txt


ls /sys/bus/w1/devices/28*
cat w1_slave

https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/


>>> import RPi.GPIO as gp 
>>> gp.setmode(g.BCM)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'g' is not defined
>>> gp.setmode(gp.BCM)
>>> gp.setup(12, gp.OUT)
>>> gp.output(12, 1)
>>> gp.output(12, 0)
>>> gp.cleanup()
>>> 
vict

### Pins
23 - Temperature
12 - Led