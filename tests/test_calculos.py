import pytest

from loja.calculos import total_carrinho

def test_carrinho_vazio_custa_zero():
    assert total_carrinho([]) == 0

def test_soma_preco_vezes_quantidade():
    # 1. preparar
    itens = [(39.90, 3), (129.90, 1)]
    # 2. agir
    total = total_carrinho(itens)
    # 3. conferir
    assert total == pytest.approx(249.60)

