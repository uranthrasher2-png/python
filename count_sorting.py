def counting_sort(A):
    if not A:
        return A
    
    # 1. Находим максимальное значение
    max_val = max(A)
    
    # 2. Создаём массив для подсчёта количества элементов
    count = [0] * (max_val + 1)
    
    # 3. Подсчитываем, сколько раз встречается каждое число
    for num in A:
        count[num] += 1

    print(count)
    
    # 4. Восстанавливаем отсортированный массив
    sorted_A = []
    for i in range(max_val + 1):
        sorted_A.extend([i] * count[i])
    
    return sorted_A


A=[1,2,5,6,3,4,7,8,0,4,3,2,1,3,4,5,6,7,8,9,0,5,4,5,2,1]

print(counting_sort(A))