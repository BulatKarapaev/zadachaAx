import numpy as np
import nashpy as nash

# Создаем платежную матрицу игры (пример)
game_matrix = np.array([
    [1, 2, 8, 4],
    [3, 3, 5, 7],
    [4, 2, 1, 5],
    [8, 5, 1, 2]
])

# Создаем игру
game = nash.Game(game_matrix)

# Находим равновесие Нэша в смешанных стратегиях
eqs = game.support_enumeration()
for eq in eqs:
    print("Оптимальная смешанная стратегия игрока A:", eq[0])
    print("Оптимальная смешанная стратегия игрока B:", eq[1])