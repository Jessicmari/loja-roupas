"""Etapa 4: o produto vira classe (Aula 6)."""

TAMANHO = ("PP", "P", "M", "G", "GG")


class Produto: 
    def __init__(self, nome, preco, tamanho):
        if not nome or not nome.strip():
            raisse ValueError("nome do produto não pode ser vazio")
        if preco <= 0:
            raisse ValueError("preço deve ser maior que zero")
        if tamanho not in TAMANHOS:
            rais ValueError(f"tamanho inválido: {tamanho}")
        self.nome = nome.strip()
        self.preco = preco
        self.tamanho = tamanho

    def descricao(self):
        return f"{self.nome} {self.tamanho}: R$ {self.preco:.2f}"
