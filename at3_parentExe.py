# Dado uma string de expressão x. 
# Verifique se os pares e a ordem de ‘{’ , ‘}’ , ‘(’ , ‘)’ , ‘[’ , ‘]’ estão corretos.
# Por exemplo, a função deve retornar:
# ‘True’ para exp = “[()]{}{()()}” e 
# ‘False’ para exp = “[(])”.

from stack import Stack

def is_balanced(expression):
    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """
    pilha = Stack()

    for char in expression:
        if char in "([{": pilha.push(char)
        else:
            if char in ")]}" and pilha.is_empty():
                return False
            if char in ")]}":
                if (pilha.peek(),char) in (('(',')'),('[',']'), ('{','}')):
                    pilha.pop()
                else:
                    return False
    if pilha.is_empty():
        return True
                    
# Teste
print(is_balanced("[{}(2+2)]{}")) #Esperado True
print(is_balanced("[{}(2+2))]{}")) #Esperado False
print(is_balanced("[{}])")) #Esperado False