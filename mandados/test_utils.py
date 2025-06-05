import pytest
from mandados import utils

def test_calcular_precio_valores_validos():
    assert utils.calcular_precio(100.00) == 100.00
    assert utils.calcular_precio(50.50) == 50.50
    assert utils.calcular_precio(0) == 0.00
    assert utils.calcular_precio("100.00") == 100.00  # str válido

def test_calcular_precio_valores_invalidos():
    assert utils.calcular_precio("abc") is None
    assert utils.calcular_precio("cien") is None
    assert utils.calcular_precio([]) is None
    assert utils.calcular_precio({}) is None
    assert utils.calcular_precio(True) is None
    assert utils.calcular_precio(False) is None
    assert utils.calcular_precio(None) is None