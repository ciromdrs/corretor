# Criando executável (windows)

## Pyinstaller

Para criar o executável do projeto, é necessária a instalação do pacote [pyinstaller](https://pyinstaller.org/en/stable/installation.html), ele será responsável por converter o código em binário .exe.

Para instalar, basta seguir o passo a passo:

```bash
pip install pyinstaller
```

Para atualizar (opcional)

```bash
pip install --upgrade pyinstaller
```

Estando na pasta do arquivo `corretor.py` execute:

```bash
 pyinstaller --onefile --noconsole corretor.py
```

A flag `--onefile` vai fazer com que o executavel seja apenas um arquivo executal de extensão .exe.

A flag `--noconsole` vai fazer com que o terminal/console que seria aberto ao executar o programa fique em segundo plano. Fazendo com que apenas a janela no corretor seja aberta para o usuário.

Após isso, serão geradas duas pastas, `build` e `dist`, dentro da pasta segunda pasta, estará o executável `corretor.exe`.

## Uso do corretor

Para usar o corretor, ainda se fará necessário o mesmo arquivo `config.json` e os arquivos python das questões.

### Exemplo

Estrutura de diretórios para que o projeto funcione corretamente.

```
/pasta-do-corretor
|-- corretor.exe
|-- config.json
|-- q1.py
|-- q2.py
```
