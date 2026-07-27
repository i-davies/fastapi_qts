from app.classificacao.classificador import classificador_nota


def test_nota_invalida_abaixo_de_zero():
    assert classificador_nota(-1) == "nota invalida"

def test_nota_invalida_acima_de_dez():
    assert classificador_nota(11) == "nota invalida"

def test_nota_aprovada():
    assert classificador_nota(8) == "aprovado"

def test_nota_em_recuperacao():
    assert classificador_nota(5.5) == "recuperacao"

def test_nota_reprovada():
    assert classificador_nota(3) == "reprovado"