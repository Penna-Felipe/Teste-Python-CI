import pytest
from calculadora import adicao, subtracao, multiplicacao, divisao, verDivisao

def teste_add():
    assert adicao(2, 3) == 5

def teste_sub():
    assert subtracao(5, 3) == 2

def teste_multi():
    assert multiplicacao(4, 3) == 12

def teste_div():
    assert divisao(10, 2)

def teste_verDivisao():
    with pytest.raises(ValueError):
        verDivisao(10, 0)