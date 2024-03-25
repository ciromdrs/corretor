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
    
    def test_correcao_ler_config(self, fxt_atividade):
        '''Testa Correcao.ler_config.'''
        correcao = fxt_atividade.questoes[0].correcoes[0]
        verificacao = correcao.verificacoes[0]
        
        assert correcao.entrada == 'hello\n'
        assert correcao.args == 'hello'
        assert correcao.msg_erro == 'Mensagem de erro padrão.'
        assert len(correcao.verificacoes) == 1
        assert verificacao['func_expect'] == 'testar_regex'
        assert verificacao['args_expect'] == 'hello'

