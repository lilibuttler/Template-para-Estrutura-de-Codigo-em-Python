# Documentação do Meu Projeto

✅ os → Funções para manipular o sistema de arquivos (criar pastas, checar diretórios).
✅ subprocess → Executa comandos de terminal via Python (git, pip etc).
✅ sys → Acessa informações do interpretador Python, aqui usado para criar venv.
✅ platform → Detecta o sistema operacional (Windows, Linux, macOS) e adapta comandos.


ESTRUTURA = [
    "meu_projeto/",               # Pasta principal: código-fonte.
    "meu_projeto/__init__.py",    # Torna a pasta um "package" Python.
    "meu_projeto/core.py",        # Arquivo com funções principais.
    "meu_projeto/utils.py",       # Arquivo para funções auxiliares.
    
    "tests/",                     # Pasta de testes unitários.
    "tests/__init__.py",          # Torna a pasta um pacote de testes.
    "tests/test_core.py",         # Teste para a função `executar_algo`.
    
    "scripts/",                   # Scripts auxiliares.
    "scripts/run.py",             # Ponto de entrada para executar o projeto.
    
    "docs/",                      # Documentação do projeto.
    "docs/index.md",              # Arquivo inicial de documentação (Markdown).
    
    ".gitignore",                 # Ignora arquivos e pastas no controle de versão.
    ".env",                       # Arquivo típico para variáveis de ambiente.
    "requirements.txt",           # Lista de dependências do projeto.
    "README.md",                  # Descrição do projeto (Markdown).
    "setup.py",                   # Arquivo clássico de instalação (pip install).
    "pyproject.toml",             # Configurações modernas (formatadores, etc).
    "Makefile",                   # Automatiza comandos comuns (make run, make test).
    "LICENSE"                     # Arquivo de licença (ex: MIT).
]

Esses são modelos mínimos, prontos para inicializar:

✅ .gitignore → evita versionar coisas desnecessárias (venv, logs, pyc).
✅ README.md → explicação inicial do projeto.
✅ requirements.txt → dependências para instalar.
✅ setup.py → define como o projeto pode ser instalado.
✅ pyproject.toml → configura ferramentas de formatação e lint.
✅ Makefile → facilita rodar comandos comuns com make.
✅ LICENSE → define direitos autorais.

Exemplos importantes:
core.py → função executar_algo() → lógica principal.
test_core.py → usa pytest para garantir que executar_algo() funciona.
run.py → script para rodar o projeto, chamando core.


⚙️ Funções do script

✅ criar_estrutura()

O que faz?

Cria todas as pastas e arquivos da lista ESTRUTURA.
Insere conteúdo base (se tiver) conforme CONTEUDOS.

Como?

Verifica se o caminho termina com / → cria pasta.
Senão → cria arquivo com o conteúdo definido.

🧠 Insight: Automatiza o esqueleto do projeto!

✅ inicializar_git()

O que faz?

Executa:

git init → inicializa repositório.

git add . → adiciona todos os arquivos.

git commit → cria commit inicial.

Como?

Usa subprocess.run para rodar comandos nativos do Git.

✅ criar_venv()

O que faz?

Cria ambiente virtual Python (venv/).

Como?

Executa: python -m venv venv

🧠 Por quê?

Isola as dependências do projeto, evita conflito com outros projetos.

✅ ativar_venv_cmd()

O que faz?

Sugere o comando certo para ativar o venv de acordo com o sistema operacional:
Windows → venv\Scripts\activate
Unix → source venv/bin/activate

💡 Observação:

Não dá para ativar venv dentro de um script. Só pode sugerir para o usuário.

✅ instalar_dependencias()

O que faz?

Instala todas as dependências listadas no requirements.txt.

Como?

Detecta se é Windows ou Unix.

Usa o pip do ambiente virtual:

pip install -r requirements.txt

🔥 Fluxo principal (__main__)

python

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

Cria estrutura
Inicializa Git
Cria venv
Instala dependências
Sugere como ativar venv
Mostra comandos make úteis

🎯 Resumo Visual:

arduino
Copiar
Editar
├── meu_projeto/
│   ├── __init__.py
│   ├── core.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
├── scripts/
│   └── run.py
├── docs/
│   └── index.md
├── .gitignore
├── .env
├── requirements.txt
├── README.md
├── setup.py
├── pyproject.toml
├── Makefile
├── LICENSE
└── venv/

🚀 Resumo ultra-rápido:

✅ Automatiza tudo
✅ Cria ambiente isolado
✅ Deixa pronto para versionar
✅ Executável via make
✅ Documentado

🗺️ Fluxograma do Script de Estruturação de Projeto Python

[Início]
   |
   v
[criar_estrutura()]
   |
   v
[inicializar_git()]
   |
   v
[criar_venv()]
   |
   v
[instalar_dependencias()]
   |
   v
[ativar_venv_cmd()]
   |
   v
[Sugere comando para ativar venv]
   |
   v
[Exibe comandos make: install, test, run]
   |
   v
[Fim: Estrutura completa criada!]

🎨 Explicação das Etapas:
✅ criar_estrutura()
➡️ Cria todas as pastas e arquivos conforme ESTRUTURA e CONTEUDOS.

✅ inicializar_git()
➡️ Executa:

git init

git add .

git commit -m "Projeto inicial gerado automaticamente"

✅ criar_venv()
➡️ Cria ambiente virtual isolado (venv/).

✅ instalar_dependencias()
➡️ Instala os pacotes do requirements.txt usando o pip do venv.

✅ ativar_venv_cmd()
➡️ Detecta o sistema operacional e sugere o comando correto para ativar o ambiente virtual.

✅ Mensagens finais:
➡️ Exibe instruções:

Como ativar o venv

Como usar make para rodar o projeto, instalar ou testar.

💥 Fluxo rápido:

Criar Estrutura → Inicializar Git → Criar venv → Instalar dependências → Sugerir ativação → Exibir
