from gpiozero import LED
from time import sleep

led1 = LED(19)

for _ in range(0):  # Cyklus se opakuje 10x
    led1.on()
    sleep(0.1)
    led1.off()
    sleep(8)
    led1.on()
    sleep(0.1)
    led1.off()
exit(0)
