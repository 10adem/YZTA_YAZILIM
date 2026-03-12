#x = 5
#y = 4
#print(x + y)

benim_listem = [10,20,30,40,50,60]

#if __name__ == '__main__':
    #print("loop başlıyor")
    #for num in benim_listem:
        #print(num)
    #print("loop bitti")

import time

def my_func_1():
    print("1. fonksiyon başlıyor")
    time.sleep(5)
    print("1. fonksiyon bitti")
    return 5

def my_func_2():
    print("2. fonksiyon başlıyor")
    time.sleep(5)
    print("2. fonksiyon bitti")
    return 10

if __name__ == '__main__':
    x = my_func_1()
    y = my_func_2()

    print(f"my func 1'in çalışması sonucu x'in değeri {x}")
    print(f"my func 2'nin çalışması sonucu y'nin değeri {y}")