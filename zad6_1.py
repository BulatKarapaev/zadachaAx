def stroka_min(matrix):
    min_values = []  # Создаем пустой список для хранения
    for row in matrix:
        min_value = min(row)
        min_values.append(min_value)  # Добавляем его в список

    return min_values
def max_find(list):
    max_number = list[0]
    for num in list:
        if num > max_number:
            max_number = num
    return max_number
def stolbech_max(matrix):
    max_values = []
    transposed_matrix = zip(*matrix)
    for column in transposed_matrix:
         max_value = max(column)
         max_values.append(max_value)
    return max_values
def min_find(list):
    min_number = list[0]
    for num in list:
        if num < min_number:
            min_number = num
    return min_number

# Пример использования
game_matrix = [
    [4, 5, 6, 7],
    [2, 3, 4, 5],
    [7, 6, 8, 10],

]

result = stroka_min(game_matrix)
result_max = max_find(result)
result2 = stolbech_max(game_matrix)
result_min = min_find(result2)
print(f"Минимальные числа в каждой строке матрицы: {result}")
print(f"Максимальное число в каждом столбце матрицы: {result2}")
print(f"Максимальное минимальное чилсло в строке : {result_max}")
print(f"Минимальное максимальное чиcло в столбце : {result_min}")

if result_min == result_max:
     print(f"Седловая точка = {result_min}")
else:
     print("Седловая точка не найдена ")