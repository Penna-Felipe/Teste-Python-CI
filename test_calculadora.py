import pytest
from calculadora import adicao, subtracao, multiplicacao, divisao, verDivisao

def test_add():
    assert adicao(2, 3) == 5

def test_sub():
    assert subtracao(5, 3) == 2

def test_multi():
    assert multiplicacao(4, 3) == 12

def test_div():
    assert divisao(10, 2)

def test_verDivisao():
    with pytest.raises(ValueError):
        verDivisao(10, 0)