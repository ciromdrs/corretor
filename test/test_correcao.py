'''Testa a classe Correcao.'''

import pytest

from . import fxt_atividade, TEST_DIR


# FIXTURES

@pytest.fixture
def fxt_correcao(fxt_atividade):
    return fxt_atividade.questoes[0].correcoes[0]


# CASOS DE TESTE

class TestCorrecao:
    def test_ler_config(self, fxt_correcao):
        '''Testa o método ler_config.'''
        correcao = fxt_correcao
        verificacao = correcao.verificacoes[0]
        
        assert correcao.entrada == 'hello\n'
        assert correcao.args == 'hello'
        assert correcao.msg_erro == 'Mensagem de erro padrão.'
        assert len(correcao.verificacoes) == 1
        assert verificacao['func_expect'] == 'testar_regex'
        assert verificacao['args_expect'] == 'hello'
        assert correcao.diretorio == f'{TEST_DIR}/data'
    
    def test_testar_regex(self, fxt_correcao):
        '''Testa o método testar_regex.'''
        correcao = fxt_correcao

        res, codigo, resposta, msg_erro = correcao.corrigir()

        assert res == True
        assert resposta == 'hello\n'
        assert msg_erro == ""
        assert codigo == 0
