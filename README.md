# MathParser

Analisador léxico e sintático simples usando biblioteca [Sly](https://sly.readthedocs.io/en/latest/sly.html)

> Referência: [https://sed-paris.gitlabpages.inria.fr/developer-meetups/2019-09-24/sly-titeux.pdf](https://sed-paris.gitlabpages.inria.fr/developer-meetups/2019-09-24/sly-titeux.pdf)

---

## Instalação

### 1. Clonar o projeto

    git clone https://github.com/fahadkalil/MathParser.git
    cd MathParser

### 2. Criar e ativar o virtualenv para o projeto

#### Windows (cmd)

      python -m venv .venv
      .venv/Scripts/activate.bat

#### Windows (PowerShell)

      python -m venv .venv
      .venv/Scripts/Activate.ps1

#### Linux / MacOS
  
      python -m venv .venv
      source .venv/bin/activate

---

### 3. Instalar dependências

    pip install sly

### 4. Rodar o projeto (com o venv ativado)

    python main.py
