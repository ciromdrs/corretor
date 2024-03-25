import os, pytest

from src.corretor.corretor import Atividade

# Diretório deste script
TEST_DIR = os.path.dirname(os.path.realpath(__file__))


# FIXTURES

@pytest.fixture
def fxt_atividade():
    atividade = Atividade.ler_arquivo_config(f'{TEST_DIR}/data/config.json')
    return atividade