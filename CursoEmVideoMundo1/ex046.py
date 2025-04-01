"""
Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos o estouro de fogos de artíficio, indo
de 10 até 0, com uma pausa de 1 segundo entre eles.

"""
import time
for count in range(10, -1, -1):
    print(count)
    time.sleep(1)
print("BUM! POOW! POPOP!")