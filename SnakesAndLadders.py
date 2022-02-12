import numpy as np

M = np.array([
    [0, .5, 0, .5, 0, 0, 0],
    [0, 0, .5, .5, 0, 0, 0],
    [0, 0, 0, .5, .5, 0, 0],
    [0, 0, 0, 0, .5, .5, 0],
    [0, 0, 0, 0, .5, .5, 0],
    [0, 0, 0, 0, .5, 0, .5],
    [0, 0, 0, 0, 0, 0, 1]
])

print('Matriz de probabilidades inicial:')

print(M)

jogada_inicial = np.array([[1], [0], [0], [0], [0], [0], [0]])

print('\nJogada inicial:')
print(jogada_inicial)

rodadas = int(input('\nDigite a quantidade de rodadas posteriores: '))

probs = np.linalg.matrix_power(M, rodadas)


print(f'\nProbabilidades daqui {rodadas} rodadas será:')

print(probs)

prever_resultado = np.matmul(np.transpose(probs), jogada_inicial)

print('\nPrevisão:')
print(prever_resultado)
