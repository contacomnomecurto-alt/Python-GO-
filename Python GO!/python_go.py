
import io
import json
import re
import sys
import tokenize
from pathlib import Path

VERSION = "0.1.7"

BASE = Path(__file__).resolve().parent
PASTA_PATCHES = BASE / "patches"
PASTA_PROGRAMAS = BASE / "programas"


def carregar_patch(nome):
    caminho = PASTA_PATCHES / f"{nome}.pgpatch"

    if not caminho.is_file():
        raise RuntimeError(
            f"Patch obrigatório não encontrado: {nome}"
        )

    dados = json.loads(caminho.read_text(encoding="utf-8"))

    if dados.get("id") != nome:
        raise RuntimeError("O identificador do patch é inválido.")

    if not isinstance(dados.get("keywords"), dict):
        raise RuntimeError("O patch não possui palavras-chave válidas.")

    return dados


def traduzir(codigo, palavras):
    linhas = codigo.splitlines(keepends=True)
    deslocamentos = [0]
    for linha in linhas:
        deslocamentos.append(deslocamentos[-1] + len(linha))

    substituicoes = []
    tokens = tokenize.generate_tokens(io.StringIO(codigo).readline)
    for token in tokens:
        if token.type != tokenize.NAME:
            continue

        linha = linhas[token.start[0] - 1]
        prefixo = linha[:token.start[1]]
        espacos = re.match(r"[ \t]+", linha[token.end[1]:])
        if (
            token.string == "variavel"
            and re.fullmatch(r"[ \t]*", prefixo)
            and espacos
        ):
            fim = deslocamentos[token.end[0] - 1] + token.end[1] + len(espacos.group())
            inicio = deslocamentos[token.start[0] - 1] + token.start[1]
            substituicoes.append((inicio, fim, ""))
            continue

        substituto = palavras.get(token.string)
        if substituto is None:
            continue

        inicio = deslocamentos[token.start[0] - 1] + token.start[1]
        fim = deslocamentos[token.end[0] - 1] + token.end[1]
        substituicoes.append((inicio, fim, substituto))

    for inicio, fim, substituto in reversed(substituicoes):
        codigo = codigo[:inicio] + substituto + codigo[fim:]

    return codigo


def executar(nome):
    arquivo = Path(nome)

    if arquivo.suffix != ".pgo":
        arquivo = arquivo.with_suffix(".pgo")

    if not arquivo.is_absolute():
        candidatos = (
            arquivo,
            BASE / arquivo,
            PASTA_PROGRAMAS / arquivo,
        )
        arquivo = next(
            (candidato for candidato in candidatos if candidato.is_file()),
            PASTA_PROGRAMAS / arquivo,
        )

    if not arquivo.is_file():
        raise RuntimeError(
            f"Programa não encontrado: {arquivo.name}"
        )

    codigo = arquivo.read_text(encoding="utf-8")

    correspondencia = re.match(
        r'\s*idioma\("([A-Za-z0-9_-]+)"\)\s*',
        codigo
    )

    if not correspondencia:
        raise RuntimeError(
            'Declare o patch com idioma("PGO-PT-BR").'
        )

    nome_patch = correspondencia.group(1)
    patch = carregar_patch(nome_patch)

    codigo = codigo[correspondencia.end():]
    codigo = traduzir(codigo, patch["keywords"])

    ambiente = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
            "list": list,
            "dict": dict,
            "min": min,
            "max": max,
            "sum": sum,
            "abs": abs
        }
    }

    exec(compile(codigo, str(arquivo), "exec"), ambiente)


def listar():
    if not PASTA_PROGRAMAS.is_dir():
        raise RuntimeError("A pasta programas não existe.")

    arquivos = sorted(PASTA_PROGRAMAS.glob("*.pgo"))

    if not arquivos:
        print("Nenhum programa encontrado.")
        return

    for arquivo in arquivos:
        print(arquivo.stem)


def main():
    if len(sys.argv) < 2:
        print("Python GO!", VERSION)
        print("Comandos: executar <nome> | listar")
        return

    comando = sys.argv[1].lower()

    try:
        if comando == "executar":
            if len(sys.argv) != 3:
                raise RuntimeError(
                    "Uso: python python_go.py executar ola"
                )

            executar(sys.argv[2])

        elif comando == "listar":
            listar()

        else:
            raise RuntimeError(
                f"Comando desconhecido: {comando}"
            )

    except Exception as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
