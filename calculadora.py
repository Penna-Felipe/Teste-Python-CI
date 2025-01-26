def adicao (a, b):
    return a + b

def subtracao (a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def verDivisao (a, b):
    if b == 0:
        raise ValueError ("NAO PODE DIVIDIR POR ZERO")

def divisao (a, b):
    verDivisao(a, b)
    return a / b
