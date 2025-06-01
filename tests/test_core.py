import pytest
from meu_projeto import core

def test_executar_algo():
    resultado = core.executar_algo()
    assert resultado == "Sucesso"
