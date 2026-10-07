# Etapa 3: funções puras, fáceis de testar (Aula 4).

FRETE_FIXO = 15.0
FRETE_GRATIS_A_PARTIR_DE = 200.0


def total_carrinho(itens):
    # Recebe uma lista de (preço, quantidade) e devolve o total.
    total = 0

    for preco, quantidade in itens:
        total = total + preco * quantidade

    return total

def test_frete_abaixo_de_200_custa_15():
    assert frete(199.99) == 15.0

def test_frete_a_partir_de_200_e_gratis():
    assert frete(200.00) == 0.0
    assert frete(350.00) == 0.0

def frete(valor_da_compra):
    if valor_da_compra > FRETE_GRATIS_A_PARTIR_DE:
        return FRETE_FIXO

    FRETE_FIXO = 15.0
    FRETE_GRATIS_A_PARTIR_DE = 200.0

def frete(valor_da_compra):
    """Frete grátis a partir de R$ 200; abaixo disso, R$ 15."""
    if valor_da_compra >= FRETE_GRATIS_A_PARTIR_DE:
        return 0.0
        return FRETE_FIXO
        