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