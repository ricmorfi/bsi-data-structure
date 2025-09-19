from stack import Stack

class MinStack(Stack):
    """
    Classe MinStack implementada herdando Stack.
    Permite retornar o valor mínimo em o(1).
    """
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def push(self, data):
        """
        Empilha (push) um novo elemento na pilha.
        Preservando o funcionamento do get_min().
        """
        self.singly_linked_list.insert_at_top(data)
        if self.min_stack.is_empty():
            self.min_stack.push(data)
        elif self.min_stack.singly_linked_list.peek() >= data:
            self.min_stack.push(data)

    def pop(self):
        """
        Desempilha (pop) o elemento do topo da pilha e retorna seu valor.
        Preservando o funcionamento do get_min().
        """
        if self.singly_linked_list.peek() == self.min_stack.singly_linked_list.peek():
            self.min_stack.pop()
            data = self.singly_linked_list.delete_from_top()
        else:
            data = self.singly_linked_list.delete_from_top()
        return data
    
    def get_min(self):
        """
        Verifica e retorna o menor valor da pilha.
        """
        if self.min_stack.is_empty():
            raise IndexError("Estrutura Vazia - Sem valor mínimo")
        return self.min_stack.singly_linked_list.peek()
