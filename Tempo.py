import numpy as np

print('Estados das probabilidades:\n')

print('Estado 0: Sol')
print('Estado 1: Chuva\n')

estados = {
    1: np.array([1, 0]),
    2: np.array([0, 1])
}

M = np.array([
    [.9, .1],
    [.5, .5]
])

print('Matriz de probabilidades inicial:')

print(M)

dia_atual = int(
    input('\nDigite o estado atual:\n1-Dia ensolarado\n2-Dia chovendo\n'))

if dia_atual == 1:
    print('\nHoje o dia está ensolarado, com estado inicial:')
else:
    print('\nHoje o dia está chovendo, com estado inicial:')

print(estados[dia_atual])

dia = int(input('\nDigite a quantidade de dias posteriores desejada: '))

probs = np.linalg.matrix_power(M, dia)


print(f'\nProbabilidades daqui {dia} dias será:')

print(probs)

prever_dia = np.matmul(np.transpose(probs), estados[dia_atual])

print(f'\nProbabilidade de fazer sol será de {prever_dia[0]}')
print(f'Probabilidade de chover será de {prever_dia[1]}')
