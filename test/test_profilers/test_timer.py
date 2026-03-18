import pytest

from time import sleep
from puma.profilers import Timer
from hypothesis import given, strategies as st


# Mock per catturare l'output dello stream
class MockStream:
    def __init__(self):
        self.message = ""
    def __call__(self, msg: str):
        self.message = msg


legitimate_chars = st.characters(whitelist_categories=('Lu', 'Ll'),
                                min_codepoint=65, max_codepoint=90)

text_strategy = st.text(alphabet=legitimate_chars, min_size=1,
                        max_size=15)


@given(name=text_strategy)
def test_timer_context_manager(name):
    """Verifica che il timer funzioni correttamente come context manager."""
    mock = MockStream()
    with Timer(name, mock):
        sleep(0.01)  # Breve pausa per garantire un tempo > 0
    
    assert name in mock.message
    assert "elapsed:" in mock.message
    # Estrae il valore numerico e verifica che sia positivo
    elapsed_time = float(mock.message.split(": ")[1])
    assert elapsed_time >= 0.01


@given(name=text_strategy)
def test_timer_decorator(name):
    """Verifica che il timer funzioni correttamente come decoratore."""
    mock = MockStream()

    @Timer(name, mock)
    def decorated_func():
        sleep(0.01)
        return "done"

    result = decorated_func()
    elapsed_time = float(mock.message.split(": ")[1])
    
    assert result == "done"
    assert name in mock.message
    assert elapsed_time >= 0.01


def test_timer_exception_handling():
    """Verifica che il timer registri il tempo anche se viene lanciata un'eccezione."""
    mock = MockStream()
    try:
        with Timer("ErrorTest", mock):
            sleep(0.01)
            raise ValueError("Boom!")
    except ValueError:
        pass
    
    assert "ErrorTest" in mock.message
    assert "elapsed:" in mock.message