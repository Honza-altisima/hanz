from gpiozero import LED
from time import sleep

led1 = LED(23)

for _ in range(1):  # Cyklus se opakuje 10x
    led1.on()
    sleep(0.1)
    led1.off()
    sleep(0.1)
    led1.on()
    sleep(0.1)
    led1.off()
exit(0)
