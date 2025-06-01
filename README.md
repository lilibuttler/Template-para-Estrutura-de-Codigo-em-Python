# Meu Projeto

Descrição do projeto.

Este projeto automatiza a criação de uma estrutura padrão para projetos Python, incluindo:
✅ organização de diretórios;
✅ arquivos essenciais;
✅ ambiente virtual;
✅ controle de versão com Git e
✅ instalação de dependências.

Ideal para quem quer iniciar novos projetos com uma base sólida e boas práticas de desenvolvimento!

🚀 O que este script faz?

✅ Cria a seguinte estrutura de diretórios:

meu_projeto/ com arquivos de código e utilitários
tests/ com arquivos de testes
scripts/ com arquivos de execução
docs/ para documentação

✅ Gera automaticamente arquivos importantes:

.gitignore
README.md
requirements.txt
setup.py
pyproject.toml
Makefile
LICENSE

✅ Inicializa um repositório Git com commit inicial
✅ Cria um ambiente virtual (venv/)
✅ Instala as dependências listadas no requirements.txt
✅ Exibe instruções finais para ativar o ambiente virtual e rodar comandos úteis

⚙️ Como usar
Salve o arquivo gerar_estrutura.py em uma pasta vazia do seu computador.
Abra o terminal (ou prompt de comando) nessa pasta.
Execute o script com: python gerar_estrutura.py


✅ O que acontece depois?
A estrutura completa será criada.
Um ambiente virtual (venv/) será configurado.
As dependências serão instaladas automaticamente.

💡 Como ativar o ambiente virtual

No Windows: venv\Scripts\activate
No Linux/MacOS: source venv/bin/activate

🛠️ Comandos úteis com Makefile
Após ativar o ambiente virtual, você pode usar:

make install   # Instalar dependências  
make test      # Rodar os testes automatizados  
make lint      # Verificar estilo do código  
make format    # Formatar o código com Black  
make run       # Executar o script principal  

📚 Exemplo de execução do projeto
make install
make run
Saída esperada:
nginx

📝 Licença
MIT License

🤓 Observação
Este projeto é um template minimalista e automatizado, ideal para agilizar o início de novos projetos Python com qualidade, organização e boas práticas desde o primeiro commit.
