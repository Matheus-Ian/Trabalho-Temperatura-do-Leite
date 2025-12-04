import machine
import onewire
import ds18x20
import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Inicialização do OLED
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

# Pinos dos componentes
PIN_SENSOR = 4
PIN_LED_OK = 15
PIN_LED_ALERT = 2
PIN_BUZZER = 13

# Inicializando hardware
dat = Pin(PIN_SENSOR)
ds = ds18x20.DS18X20(onewire.OneWire(dat))
roms = ds.scan()

led_ok = Pin(PIN_LED_OK, Pin.OUT)
led_alert = Pin(PIN_LED_ALERT, Pin.OUT)
buzzer = Pin(PIN_BUZZER, Pin.OUT)

TEMP_MAX = 4.0

def alerta():
    led_ok.value(0)
    led_alert.value(1)
    buzzer.value(1)
    time.sleep(0.2)
    buzzer.value(0)

def temperatura_ok():
    led_alert.value(0)
    buzzer.value(0)
    led_ok.value(1)

while True:
    ds.convert_temp()
    time.sleep(0.8)
    temp = ds.read_temp(roms[0])

    print("Temperatura:", temp, "°C")

    # Exibe no display
    oled.fill(0)
    oled.text("Temp:", 0, 0)
    oled.text(str(temp) + " C", 0, 15)
    oled.show()

    # Verificação da temperatura
    if temp > TEMP_MAX:
        alerta()
    else:
        temperatura_ok()
