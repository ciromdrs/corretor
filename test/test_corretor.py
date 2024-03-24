import json, unittest

from src.corretor.corretor import Atividade, Questao, Correcao

from . import TEST_DIR

class TestLerConfig(unittest.TestCase):
    def setUp(self):
        arq_config = open(f'{TEST_DIR}/data/config.json')
        config = json.load(arq_config)
        arq_config.close()
        self.atividade = Atividade.ler_config(config)

    def test_atividade_ler_config(self):
        '''Testa Atividade.ler_config.'''
        assert self.atividade.titulo == "Atividade 1"
