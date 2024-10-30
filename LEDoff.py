from gpiozero import LED
from time import sleep

led1 = LED(21)
led2 = LED(19)

for _ in range(1):  # Cyklus se opakuje 10x
    led1.off()
    led2.off()
    sleep(0.1)
exit(0)
