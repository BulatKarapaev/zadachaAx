# Матрица игры
game_matrix = [
    [4, 5, 6, 7],
    [2, 3, 4, 5],
    [7, 6 , 8 ,10],


]

# Нижняя цена игры (minmax)
lower_price = min(max(row) for row in game_matrix)
print(lower_price)

# Верхняя цена игры (maxmin)
upper_price = max(min(col) for col in zip(*game_matrix))
print(upper_price)
# Проверка наличия седловой точки
if lower_price == upper_price:
    print(f"Седловая точка найдена. Цена игры: {lower_price}")
else:
    print("Седловая точка отсутствует.")
