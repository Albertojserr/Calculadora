class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, a, b):
        self.value = a + b
    def min(self,a,b):
        self.value=a-b
    def plus(self,a,b):
        self.value=a*b
    def div(self,a,b):
        self.value=a/b
    def factorial(self,a):
        if a<0:
            self.value="No se puede hacer un factorial de un número negativo"
        else:
            fact = 1
            for i in range(1,a+1):
                fact = fact * i
            self.value=fact