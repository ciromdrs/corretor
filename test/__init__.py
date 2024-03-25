import json, os, pytest

from src.corretor.corretor import Atividade

# Diretório deste script
TEST_DIR = os.path.dirname(os.path.realpath(__file__))


# FIXTURES

@pytest.fixture
def fxt_atividade():
    arq_config = open(f'{TEST_DIR}/data/config.json')
    config = json.load(arq_config)
    arq_config.close()
    atividade = Atividade.ler_config(config)
    return atividade