import json, unittest

from src.corretor.corretor import Atividade, Questao, Correcao

from . import TEST_DIR

class TestLerConfig(unittest.TestCase):
    def setUp(self):
        arq_config = open(f'{TEST_DIR}/data/config.json')
        config = json.load(arq_config)
        arq_config.close()
        self.atividade = Atividade.ler_config(config)

    def test_titulo(self):
        '''Testa se lê o título.'''
        self.assertEqual(self.atividade.titulo, "Atividade 1")

'''
{
    "titulo" : "Atividade 1",
    "comando" : "python",
    "msg_erro" : "Mensagem de erro padrão.",
    "func_expect" : "testar_regex",
    "pontos" : 0,
    "questoes" : [
        {
            "descricao" : "Questão 1",
            "script" : "q1.py",
            "correcoes" : [
                {
                    "entrada" : "hello\n",
                    "args" : "hello",
                    "verificacoes" : [
                        { "args_expect" : "hello" }
                    ]
                },
                {
                    "entrada" : "não\n",
                    "args" : "não",
                    "verificacoes" : [
                        { "args_expect" : "não" }
                    ]
                },
                {
                    "entrada" : "olá\n",
                    "args" : "olá",
                    "verificacoes" : [
                        { "args_expect" : "isto deveria falhar" }
                    ]
                }
            ]
        },
        {
            "descricao" : "Questão 2",
            "script" : "q2.py",
            "correcoes" : [
                {
                    "verificacoes" : [],
                    "msg_erro" : "isto deveria dar erro de sintaxe"
                }
            ]
        },
        {
            "descricao" : "Questão 3",
            "script" : "arquivo_ausente.py",
            "correcoes" : [
                {
                    "verificacoes" : [],
                    "msg_erro" : "Arquivo intencionalmente ausente."
                }
            ]
        }
   ]
}
'''