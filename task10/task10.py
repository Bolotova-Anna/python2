# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и 
# той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть.
n =int(input("введите количество монет: "))
count_or = 0
count_re = 0
for i in range(1,n+1):
    mon = int(input(f"введите 1(орел) или решка(0) для {i} -й монеты"))
    if mon ==1:
        count_or +=1
    else:
        count_re +=1
if count_or < count_re:
    print(f" минимальное количество монет {count_or}")
else:
    print(f" минимальное количество монет {count_re}")


    
