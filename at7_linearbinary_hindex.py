def linear_h_index(arr):
    '''
    Calcula o índice-h de forma linear.
    '''
    for i in range(len(arr)):
        if arr[i] < i + 1:
            print(f"Índice-h: {i}")
            return i
    print(f"Índice-h: {len(arr)}")    
    return len(arr)


def binary_h_index(arr):
    '''
    Calcula o índice-h de forma binária.
    '''
    left, right = 0, len(arr) - 1
    while left <= right:
        meio = (left + right) // 2
        if arr[meio] >= meio + 1:
            left = meio + 1
        else:
            right = meio - 1
    print(f'Índice-h: {left}')
    return left

citacoes = [8, 4, 4, 4, 4, 2, 1, 0]

# (a) Resolvendo com Busca Linear
print("Utilizando Busca Linear")
print(linear_h_index(citacoes))

# (b) Resolvendo com Busca Binária
print("Utilizando Busca Binária")
print(binary_h_index(citacoes))

