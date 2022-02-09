class stack:
    def __init__(self):
        self.pila = []
   
    def push(self, elem):
    # @param elem: any type of data
    # @return None
        self.pila.append(elem)
    
    def pop(self):
    # @return None
        return self.pila.pop()
    
    def top(self):
    # @return any type of data
        return self.pila[-1]
    
    def empty(self):
    # ritorna vero se la coda e' vuota falso altrimenti
    # return bool
        if len(self.pila) == 0:
            return True
        else:
            return False


class queue:
    def __init__(self):
        self.coda = []
    
    def add(self, elem):
    # aggiunge un'ultimo elemento alla coda
    # @param elem: any type of data
    # @return None
        self.coda.append(elem)
    
    def out(self):
    # scarta il primo elemento della coda
    # @return None
        return self.coda.pop(0)
    
    def first(self):
    # ritorna il primo elemento della coda
    # @return any type of data
        return self.coda[0]
    
    def last(self):
    # ritorna l'ultimo elemento della coda
    # @return any type of data
        return self.coda[-1]
    
    def empty(self):
    # ritorna vero se la coda e' vuota falso altrimenti
    # return bool
        if len(self.coda) == 0:
            return True
        else:
            return False
