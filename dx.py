from pynput.keyboard import Key, Controller
import time

total_point = 0

while(True):
    print(total_point)
    val = input("Enter jumlah item: ")
    total_point = total_point + 3*int(val)
