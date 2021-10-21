'''Для матрицы из предыдущего задания найти:
а) евклидову норму;
б) норму Фробениуса.'''

import numpy as np

A = np.array([[1, 2, 0], [0, 0, 5], [3, -4, 2], [1, 6, 5], [0, 1, 0]])

Ne = np.linalg.norm(A, ord=2)    #  = np.max(диагональной матрицы)
Nf = np.linalg.norm(A, ord='fro') # = Норме Фробениуса диагональной матрицы (sqrt(sum(m**2)))

print(f'Евклидова норма матрицы: {Ne:.2f}')
'''Евклидова норма матрицы: 8.82'''

print(f'Норма Фробениуса матрицы: {Nf:.2f}')
'''Норма Фробениуса матрицы: 11.05'''
