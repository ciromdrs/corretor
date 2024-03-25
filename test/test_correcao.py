'''Testa a classe Correcao.'''

from src.corretor.corretor import Correcao
from . import fxt_atividade

class TestCorrecao:
    def test_ler_config(self, fxt_atividade):
        '''Testa o método ler_config.'''
        correcao = fxt_atividade.questoes[0].correcoes[0]
        verificacao = correcao.verificacoes[0]
        
        assert correcao.entrada == 'hello\n'
        assert correcao.args == 'hello'
        assert correcao.msg_erro == 'Mensagem de erro padrão.'
        assert len(correcao.verificacoes) == 1
        assert verificacao['func_expect'] == 'testar_regex'
        assert verificacao['args_expect'] == 'hello'