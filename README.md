# Trabalho 1 (Participação) — Meu primeiro teste com pytest

- **Disciplina:** Validação, Verificação e Teste de Software.  
- **Curso:** Análise e Desenvolvimento de Sistemas (ADS)  
- **Professor:** Osmar Betazzi Dordal  
- **Aluno:** Guilherme Lacerda A da Silva 
- **RA:** 2420864 
- **Entrega:** próxima terça-feira (até 23:59)  
- **Peso:** participação (equivalente à presença)

## 1) Objetivo
Criar um projeto Python mínimo, escrever **1 função** e **1 teste automatizado** com `pytest`, e registrar evidências de execução.

## 2) Requisitos
- Python 3.11+ (ou 3.10+ se combinado em sala)
- Acesso ao terminal (PowerShell/Prompt no Windows; Terminal no Linux/macOS)

## 3) Estrutura do projeto (mínima)
Seu projeto deve ter, no mínimo:

- `src/app.py` (código)
```powershell
def get_cowboy_greeting(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("O nome precisa ser um texto.")
    
    name = name.strip()
    if not name:
        raise ValueError("O forasteiro precisa ter um nome.")
        
    return f"Howdy, {name}! Ready to code in the Wild West?"
```
- `tests/test_app.py` (teste)
```powershell
import pytest
from src.app import get_cowboy_greeting

def test_get_cowboy_greeting_valid_name():
    """Verifica se a saudação é gerada corretamente para um nome válido."""
    assert get_cowboy_greeting("Guilherme") == "Howdy, Guilherme! Ready to code in the Wild West?"

def test_get_cowboy_greeting_empty_string():
    """Verifica se a função levanta erro para string vazia ou só com espaços."""
    with pytest.raises(ValueError):
        get_cowboy_greeting("   ")
    with pytest.raises(ValueError):
        get_cowboy_greeting("")

def test_get_cowboy_greeting_non_string_input():
    """Verifica se a função levanta erro se receber números ou outros tipos."""
    with pytest.raises(TypeError):
        get_cowboy_greeting(123)
    with pytest.raises(TypeError):
        get_cowboy_greeting(None)
```
- `README.md` (este arquivo)

Sugestão de estrutura:

```
Trabalho Osmar
│
├── src/
│   └── app.py
├── tests/
│    └── test_app.py
└── README.md
```

## 4) Evidências (obrigatório)
Cole aqui a saída do comando `pytest -q` (print/copiar e colar do terminal):

```powershell
========================= test session starts =========================
collected 3 items

tests/test_app.py ...                                           [100%]

========================== 3 passed in 0.01s ==========================