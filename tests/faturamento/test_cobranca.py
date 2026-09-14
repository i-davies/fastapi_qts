import time

import pytest

from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, retorno_esperado",
    [
        # Entradas inválidas
        (0.0, "BASICO", 0, -1.0),
        (-50.0, "PREMIUM", 0, -1.0),
        (100.0, "BASICO", -1, -1.0),
        (100.0, "VIP", 0, -2.0),
        (100.0, "", 0, -2.0),
        # Pagamento em dia (dias_atraso == 0)
        (100.0, "BASICO", 0, 100),
        (100.0, "PREMIUM", 0, 90),
        (100.0, "EMPRESARIAL", 0, 80),
        # Normalização de texto
        (100.0, "    premium     ", 0, 90),
        # Atraso modera (1 a 30 dias) e valores de fronteira
        (100.0, "BASICO", 1, 105.5),
        (100.0, "PREMIUM", 10, 99.5),
        (100.0, "BASICO", 30, 120.0),
        # Atraso severo (> 30 dias) e valores de fronteira
        (100.0, "BASICO", 31, 156.0),
        (100.0, "EMPRESARIAL", 40, 137.0),
        
    ]
)
def test_processar_cobranca_funcional(
    valor_base, plano, dias_atraso, retorno_esperado
):
    assert (
        processar_cobranca(valor_base, plano, dias_atraso) == retorno_esperado
    )

def test_tempo_processamento_cobranca_nao_funcional():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "BASICO", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado == 100.0
    assert tempo_decorrido < 0.1
    