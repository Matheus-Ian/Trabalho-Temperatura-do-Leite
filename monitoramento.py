# Exemplo de leitura de temperatura simulada

import time
import random

def ler_temperatura():
    return round(20 + random.random()*5, 2)

while True:
    print("Temperatura:", ler_temperatura(), "°C")
    time.sleep(2)
