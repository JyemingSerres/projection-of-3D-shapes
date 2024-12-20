"""
Created on 12/17/2024
by Jye-Ming Serres
"""
from abc import ABC, abstractmethod
from enum import Enum

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

class StateMachine:
    """
    StateMachine doc
    """

    def __init__(self, states: list[State], default_state: State=None) -> None:
        self._states = states
        self._default_state = states[0] if default_state is None else default_state
        self._current_state = self._default_state

    @property
    def states(self) -> list[State]:
        return self._states

    @property
    def current_state(self) -> State:
        return self._current_state

    def add_transition(self, state_from: State, state_to: State, trigger: Enum) -> None:
        if trigger in state_from.transitions:
            raise ValueError("Duplicate: trigger already defined for this state")
        state_from.transitions[trigger] = state_to

    def add_transitions(self, state_from: State, state_to: State, triggers: list[Enum]) -> None:
        for trigger in triggers:
            self.add_transition(state_from, state_to, trigger)

    def update(self) -> None:
        self._current_state.update()

    def reset(self) -> None:
        self._current_state = self._default_state

    def trigger(self, trigger: Enum) -> None:
        if trigger in self._current_state.transitions:
            self.__change_state(self._current_state.transitions[trigger])

    def __change_state(self, new_state: State) -> None:
        self._current_state.exit()
        self._current_state = new_state
        self._current_state.enter()
