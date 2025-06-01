import os
import subprocess
import sys
import platform

ESTRUTURA = [
    "meu_projeto/",
    "meu_projeto/__init__.py",
    "meu_projeto/core.py",
    "meu_projeto/utils.py",
    "tests/",
    "tests/__init__.py",
    "tests/test_core.py",
    "scripts/",
    "scripts/run.py",
    "docs/",
    "docs/index.md",
    ".gitignore",
    ".env",
    "requirements.txt",
    "README.md",
    "setup.py",
    "pyproject.toml",
    "Makefile",
    "LICENSE"
]

CONTEUDOS = {
    ".gitignore": "venv/\n__pycache__/\n*.pyc\n.env\n*.log\n",
    "README.md": "# Meu Projeto\n\nDescrição do projeto.\n",
    "requirements.txt": "requests>=2.31.0\npytest>=8.0.0\npython-dotenv>=1.0.0\n",
    "setup.py": '''from setuptools import setup, find_packages

setup(
    name='meu_projeto',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0',
    ],
    entry_points={{
        'console_scripts': [
            'meu_projeto=meu_projeto.scripts.run:main',
        ],
    }},
)
''',
    "pyproject.toml": '''[tool.black]
line-length = 88

[tool.isort]
profile = "black"

[tool.flake8]
max-line-length = 88
''',
    "Makefile": '''install:
\tpip install -r requirements.txt

test:
\tpytest

lint:
\tflake8 meu_projeto tests

format:
\tblack meu_projeto tests

run:
\tpython scripts/run.py
''',
    "LICENSE": "MIT License\n\nCopyright...",
    "meu_projeto/core.py": '''def executar_algo():
    """
    Função principal do projeto.

    :return: str
    """
    return "Sucesso"
''',
    "tests/test_core.py": '''import pytest
from meu_projeto import core

def test_executar_algo():
    resultado = core.executar_algo()
    assert resultado == "Sucesso"
''',
    "scripts/run.py": '''from meu_projeto import core

def main():
    resultado = core.executar_algo()
    print(resultado)

if __name__ == "__main__":
    main()
''',
    "docs/index.md": "# Documentação do Meu Projeto\n\nAqui vai a documentação."
}

def criar_estrutura():
    print("\n🔧 Criando estrutura de pastas e arquivos...")
    for caminho in ESTRUTURA:
        if caminho.endswith('/'):
            os.makedirs(caminho, exist_ok=True)
            print(f"[DIR] {caminho}")
        else:
            dir_name = os.path.dirname(caminho)
            if dir_name and not os.path.exists(dir_name):
                os.makedirs(dir_name)
                print(f"[DIR] {dir_name}")
            with open(caminho, 'w', encoding='utf-8') as f:
                conteudo = CONTEUDOS.get(caminho, '')
                f.write(conteudo)
                print(f"[FILE] {caminho}")

def inicializar_git():
    print("\n🔧 Inicializando repositório Git...")
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Projeto inicial gerado automaticamente'])

def criar_venv():
    print("\n🔧 Criando ambiente virtual...")
    subprocess.run([sys.executable, '-m', 'venv', 'venv'])

def ativar_venv_cmd():
    # Não dá para ativar o venv dentro de script. Só sugerimos.
    if platform.system() == 'Windows':
        return 'venv\\Scripts\\activate'
    else:
        return 'source venv/bin/activate'

def instalar_dependencias():
    print("\n🔧 Instalando dependências do requirements.txt...")
    if platform.system() == 'Windows':
        pip_exec = '.\\venv\\Scripts\\pip'
    else:
        pip_exec = './venv/bin/pip'
    subprocess.run([pip_exec, 'install', '-r', 'requirements.txt'])

if __name__ == "__main__":
    criar_estrutura()
    inicializar_git()
    criar_venv()
    instalar_dependencias()

    ativacao = ativar_venv_cmd()

    print(f"\n✅ Estrutura completa criada com sucesso!")
    print(f"\n💡 Para ativar o ambiente virtual, use:\n\n    {ativacao}\n")
    print("🚀 Depois, você pode rodar:\n")
    print("    make install    # para instalar dependências")
    print("    make test       # para rodar testes")
    print("    make run        # para executar o projeto\n")
