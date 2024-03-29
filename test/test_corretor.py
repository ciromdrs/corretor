'''Testa o script corretor.py'''

from src.corretor.corretor import Atividade
from . import fxt_atividade, TEST_DIR


# TESTS

class TestLerConfig:
    
    def test_atividade_ler_arquivo_config(self):
        '''Testa Atividade.ler_arquivo_config.'''
        atividade = Atividade.ler_arquivo_config(f'{TEST_DIR}/data/config.json')
        assert atividade.titulo == "Atividade 1"
        assert len(atividade.questoes) == 3
    
    def test_atividade_ler_config(self, fxt_atividade):
        '''Testa Atividade.ler_config.'''
        atividade = fxt_atividade
        assert atividade.titulo == "Atividade 1"
        assert len(atividade.questoes) == 3
    
    def test_questao_ler_config(self, fxt_atividade):
        '''Testa Questao.ler_config.'''
        questao = fxt_atividade.questoes[0]
        
        assert questao.descricao == "Questão 1"
        assert len(questao.correcoes) == 3
        assert questao.pontos == 0
