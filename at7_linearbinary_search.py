def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        _quicksort(arr, left, pi - 1)
        _quicksort(arr, pi + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1 

def linearSearch(arr, alvo):
    '''
    Função de Busca Linear
    Percorre a lista um a um até encontrar
    '''
    for i in range(len(arr)):
        if arr[i] == alvo:
            print("Valor encontrado!")
            return i
        if arr[i] > alvo:
            print("Valor fora da lista.")
            print(f'Índice para inserção correta: {i}')
            return i
    print("Valor fora da lista")
    print(f'Índice para inserção correta: {i + 1}')
    return i + 1
        
def binarySearch(arr, alvo):
    '''
    Função de Busca Binária
    Ordena o array e realiza divisões ao meio até encontrar
    '''
    quicksort(arr)
    start, end = 0, len(arr) - 1
    while start <= end:
        meio = (start + end) // 2
        if arr[meio] == alvo:
            print("Valor encontrado.")
            return meio
        elif arr[meio] < alvo:
            start = meio + 1
        else:
            end = meio - 1
    print("Valor fora da lista.")
    print(f'Índice para inserção correta: {start}')
    return start

arr = [17,7,10,4,3,1,7]
quicksort(arr)
alvo1 = 7
alvo2 = 6

# (a) Resolvendo com Busca Linear
print("Busca Linear para os alvos 1 e 2")
print("Alvo 1:")
linearSearch(arr, alvo1)
print("Alvo 2:")
linearSearch(arr, alvo2)

# (b) Resolvendo com Busca Binária
print(f"\nBusca Binária para os alvos 1 e 2")
print("Alvo 1:")
binarySearch(arr, alvo1)
print("Alvo 2:")
binarySearch(arr, alvo2)