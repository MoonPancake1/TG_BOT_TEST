





# Дан массив положительных чисел, необходимо сделать
# так, чтобы все 0 переместились в конец но 
# порядок чисел оставался таким же

# [1, 8, 0, 3, 0] -> [1, 8, 3, 0, 0]
# [1, 8, 0, 0, 3] -> [1, 8, 3, 0, 0]

# arr = [1, 8, 0, 0, 3]
# l = -1

# for i in range(len(arr)): # O(n)
#     if arr[i] == 0 and l == -1:
#         l = i
#     elif arr[i] and l != -1:
#         arr[l] += arr[i]
#         arr[i] = 0
#         l += 1

# print(arr)

# Скорость: O(n)
# Память: O(1)
        


import threading
import time

def task(name):
    print(f"{name} начал работу")
    time.sleep(2)
    print(f"{name} завершил работу")

# Создаём два потока
t1 = threading.Thread(target=task, args=("Поток 1",))
t2 = threading.Thread(target=task, args=("Поток 2",))

t1.start()
t2.start()

t1.join()
t2.join()
print("Все потоки завершены")