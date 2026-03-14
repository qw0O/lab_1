import time
import random
import tracemalloc

#   Функция генерации случайного массива
def generate_array(n):
    return [random.randint(0, 10000) for _ in range(n)]

#   Функция замера времени
def measure_time(func, data):
    start = time.perf_counter()
    func(data) # Запускаем переданную функцию
    end = time.perf_counter()
    return end - start

#   Функция замера времени И памяти (для сортировки)
def measure_time_and_space(func, data):
    tracemalloc.start() # Начинаем следить за памятью
    start = time.perf_counter()
    
    func(data)
    
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory() # Получаем пиковое значение памяти
    tracemalloc.stop()
    
    time_taken = end - start
    space_taken_kb = peak / 1024 # Переводим байты в Килобайты
    return time_taken, space_taken_kb


#1. Проверка наличия элемента в массиве
def linear_search(arr, target=99999): 
    for x in arr:
        if x == target:
            return True
    return False


#2. Поиск второго максимального элемента
def find_second_max(arr):
    if len(arr) < 2:
        return None
    max1 = max2 = float('-inf')
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2 and x != max1:
            max2 = x
    return max2


#3. Бинарный поиск
def binary_search(arr, target=99999):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


#4. Построение таблицы умножения
def multiplication_table(n):
    # n - это не массив, а просто число (размер таблицы)
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table


#Сортировка
def insertion_sort(arr):
    arr_copy = arr.copy() 
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy




if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    
    print("--- 1. Линейный поиск ---")
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(linear_search, arr)
        print(f"n={n}: {t:.6f} сек")
        
    print("\n--- 3. Бинарный поиск ---")
    for n in sizes:
        arr = sorted(generate_array(n)) 
        t = measure_time(binary_search, arr)
        print(f"n={n}: {t:.6f} сек")
        
    print("\n--- 4. Таблица умножения ---")
    small_sizes = [10, 50, 100, 500] 
    for n in small_sizes:
        start = time.perf_counter()
        multiplication_table(n)
        end = time.perf_counter()
        print(f"n={n}: {end - start:.6f} сек")

    print("\n--- 5. Сортировка (Время и Память) ---")
    for n in sizes:
        arr = generate_array(n)
        t, space = measure_time_and_space(insertion_sort, arr)
        print(f"n={n}: Время = {t:.6f} сек, Память = {space:.2f} КБ")
