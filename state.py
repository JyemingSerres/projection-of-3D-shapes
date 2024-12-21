"""
Created on 12/17/2024
by Jye-Ming Serres
"""
from abc import ABC, abstractmethod

class State(ABC):
    """
    State doc
    """

    def __init__(self) -> None:
        self.transitions = dict()

    @abstractmethod
    def enter(self) -> None: pass

    @abstractmethod
    def update(self) -> None: pass

    @abstractmethod
    def exit(self) -> None: pass
