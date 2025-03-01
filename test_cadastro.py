import pytest
from cadastro import validar_cep, carregar_faixas_cep

@pytest.fixture
def faixas_cep():
    return carregar_faixas_cep("ceps.xlsx")

@pytest.mark.parametrize("cep, cidade, esperado", [
    ("18050-100", "Sorocaba", True),
    ("18195-000", "Capela do Alto", True),
    ("18130-020", "São Roque", True),
    ("19000-000", "Votorantim", False),
    ("99999-999", "Desconhecido", False),
])
def test_validar_cep(cep, cidade, esperado, faixas_cep):
    assert validar_cep(cep, cidade, faixas_cep) == esperado
