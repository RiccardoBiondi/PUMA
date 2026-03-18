"""
PUMA - Personal Use Macro Archive 🐾
Module: Time Benchmarking Utilities

This module provides agile tools for execution time measurement.
It features the `Timer` class, designed to be used both as a Context Manager 
and a Decorator, integrating seamlessly into any performance-critical workflow.

Example:
    Using as a Context Manager:
        with Timer("Database Query", print):
            db.execute_heavy_query()

    Using as a Decorator:
        @Timer("Algorithm Analysis", logger.info)
        def my_function():
            pass

Author: Riccardo Biondi
"""

import time
from typing import Callable, NoReturn
from contextlib import ContextDecorator

__author__ = ["Riccardo Biondi"]
__email__ = ["riccardo.biondi@proton.me"]


class Timer(ContextDecorator):
    """
    Un'utility agile per il benchmarking temporale di funzioni e blocchi di codice.

    Questa classe implementa il protocollo Context Manager e il mixin ContextDecorator,
    permettendo di misurare il tempo di esecuzione sia tramite l'istruzione `with` 
    che come decoratore di funzione.

    Attributes:
        name (str): Identificativo del timer visualizzato nell'output.
        stream (Callable[[str], NoReturn]): Funzione di callback per gestire il log 
            del risultato (es. `print` o un logger personalizzato).
        tik (float): Timestamp iniziale dell'operazione.

    Example:
        >>> with Timer("Processo Dati", print):
        >>>     # logica da misurare
        >>>     pass
        
        >>> @Timer("Mia Funzione", print)
        >>> def mia_funzione():
        >>>     pass
    """

    def __init__(self, name: str, stream: Callable[[str], NoReturn]) -> None:

        self.name: str = name
        self.tik: float = 0.
        self.stream: Callable[[str], NoReturn] = stream 

    def __enter__(self):
        self.tik = time.time()
        return self

    def __exit__(self, *exc):
        tok: float = time.time()
        elapsed: float = tok - self.tik
        self.stream(f"{self.name} elapsed: {elapsed}")

