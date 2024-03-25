import json, pytest

from src.corretor.corretor import Atividade

from . import TEST_DIR


# FIXTURES

@pytest.fixture
def fxt_atividade():
    arq_config = open(f'{TEST_DIR}/data/config.json')
    config = json.load(arq_config)
    arq_config.close()
    atividade = Atividade.ler_config(config)
    return atividade


# TESTS

class TestLerConfig:

    def test_atividade_ler_config(self, fxt_atividade):
        '''Testa Atividade.ler_config.'''
        atividade = fxt_atividade
        assert atividade.titulo == "Atividade 1"
        assert len(atividade.questoes) == 3
    
    def test_questao_ler_config(self, fxt_atividade):
        '''Testa Atividade.ler_config.'''
        questao = fxt_atividade.questoes[0]
        
        assert questao.descricao == "Questão 1"
        assert len(questao.correcoes) == 3
        assert questao.pontos == 0

