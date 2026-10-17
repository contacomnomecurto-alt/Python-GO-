# Python-GO!

Python GO!

Versão atual: 0.1.9

Python GO! é um projeto experimental de linguagem de programação inspirado em Python. Seu objetivo é permitir que programas sejam escritos com palavras-chave localizadas, como "mostrar", "se", "senao" e "para", utilizando patches de idioma.

O projeto possui um interpretador escrito em Python que lê arquivos ".pgo", identifica o idioma declarado, traduz as palavras-chave configuradas e executa o código resultante.

Funcionalidades

- Interpretador próprio para arquivos ".pgo".
- Menu interativo para executar programas, listar arquivos e sair.
- Sistema de patches de idioma ".pgpatch".
- Suporte ao patch "PGO-PT-BR" para português brasileiro.
- Tradução de palavras-chave antes da execução.
- Suporte a variáveis, condicionais e estruturas de repetição conforme as palavras-chave configuradas.
- Busca de programas e patches em diretórios do projeto.
- Mensagens de erro para problemas de leitura, localização e execução.
- Execução por meio do menu ou de comandos no terminal.

Estrutura do projeto

Python GO!/
├── python_go.py
├── README.md
├── patches/
│   ├── PGO-PT-BR.pgpatch
│   └── PGO-EN.pgpatch
└── programas/
    └── ola.pgo

    Essa é uma estrutura de referência. Mantenha no README somente os arquivos que realmente existirem no projeto.

    Como funciona?

    Os programas utilizam a extensão ".pgo". Cada programa declara o patch de idioma que deve ser utilizado por meio da instrução "idioma(...)".

    O interpretador lê o arquivo, carrega o patch correspondente, traduz as palavras-chave e executa o código usando Python.

    Exemplo de programa

    Arquivo: "programas/ola.pgo"

    idioma("PGO-PT-BR")

    variavel vida = 100

    mostrar("Bem-vindo ao Python GO!")
    mostrar("Vida:", vida)

    se vida > 0:
        mostrar("Você está vivo!")
        senao:
            mostrar("Game Over!")

            para numero em range(3):
                mostrar("GO!", numero + 1)

                Saída esperada

                Bem-vindo ao Python GO!
                Vida: 100
                Você está vivo!
                GO! 1
                GO! 2
                GO! 3

                Patches de idioma

                Os patches de idioma são arquivos JSON com a extensão ".pgpatch". Eles associam palavras-chave da linguagem às palavras-chave equivalentes do Python.

                Patch português brasileiro

                Arquivo: "patches/PGO-PT-BR.pgpatch"

                {
                  "id": "PGO-PT-BR",
                    "idioma": "Português",
                      "keywords": {
                          "mostrar": "print",
                              "se": "if",
                                  "senao": "else",
                                      "enquanto": "while",
                                          "para": "for",
                                              "em": "in",
                                                  "verdadeiro": "True",
                                                      "falso": "False",
                                                          "nulo": "None",
                                                              "e": "and",
                                                                  "ou": "or",
                                                                      "nao": "not"
                                                                        }
                                                                        }

                                                                        O identificador do patch precisa corresponder ao nome declarado no arquivo ".pgo".

                                                                        Como executar

                                                                        Inicie "python_go.py" no Python. O menu oferece três opções:

                                                                        1. Executar um programa.
                                                                        2. Listar programas disponíveis.
                                                                        3. Sair.

                                                                        Ao escolher a primeira opção, informe o nome do programa, por exemplo "ola" ou "ola.pgo".

                                                                        Também é possível executar comandos pelo terminal:

                                                                        python python_go.py listar
                                                                        python python_go.py executar ola

                                                                        Patch de atualização atual

                                                                        Versão: 0.1.9

                                                                        A versão 0.1.9 é a versão atual do Python GO!.

                                                                        O desenvolvimento recente concentrou-se em corrigir a localização dos programas e dos patches, resolver incompatibilidades nas chamadas das funções e permitir o acesso aos arquivos do projeto no Android.

                                                                        O programa "ola.pgo" foi executado com sucesso, demonstrando o funcionamento da tradução de palavras-chave, das variáveis, das condicionais e das estruturas de repetição.

                                                                        Este registro descreve a atualização atual. Ele não representa um arquivo de patch instalável separado.

                                                                        Patches de atualizações passadas

                                                                        O histórico abaixo registra a evolução conhecida do projeto. Os números de versão representam versões do interpretador, e não necessariamente arquivos de atualização independentes.

                                                                        Versão| Histórico
                                                                        0.1.0| Primeira versão do Python GO!.
                                                                        0.1.5| Versão intermediária do projeto.
                                                                        0.1.7| Versão do interpretador com execução por comandos, listagem de programas e tradução baseada em patches.
                                                                        0.1.8| Introdução do menu interativo.
                                                                        0.1.8.5| Melhorias na localização de programas e patches e nas mensagens de erro.
                                                                        0.1.8.56| Ajustes nos caminhos do projeto e correção da chamada do localizador de programas.
                                                                        0.1.9| Versão atual, com o fluxo de execução de "ola.pgo" testado com sucesso.

                                                                        As alterações específicas das versões 0.1.0 e 0.1.5 precisam ser complementadas caso exista um registro original dessas versões.

                                                                        Arquivos de atualização

                                                                        Caso sejam disponibilizados arquivos de atualização separados, eles poderão ser documentados nesta seção com seus nomes, versões de origem, versões de destino e instruções de instalação.

                                                                        Os arquivos ".pgpatch" utilizados para traduzir palavras-chave são patches de idioma e não devem ser confundidos com atualizações do interpretador.

                                                                        Compatibilidade e segurança

                                                                        - O interpretador requer Python.
                                                                        - O acesso aos arquivos depende da localização do projeto e das permissões do sistema operacional.
                                                                        - O sistema de tradução por palavras-chave não constitui uma sandbox segura para código não confiável.
                                                                        - Os patches devem conter JSON válido e um identificador compatível com o programa que os utiliza.

                                                                        Objetivo

                                                                        O Python GO! busca explorar uma maneira de programar usando palavras-chave localizadas, mantendo o Python como base de execução e permitindo a expansão da linguagem por meio de patches.
-------------------------
# Filosofia:

Uma linguagem. Vários idiomas. Um núcleo.

Python GO! — programação do seu jeito!


Nota do desenvolvedor: O Python foi criado para ser fácil de entender para o povo nativo da América do Norte, o Python GO! para o mundo inteiro.