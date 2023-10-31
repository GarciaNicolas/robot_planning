from abc import ABC, abstractmethod

from setuptools.wheel import Wheel

from instructionStrategy import InstructionStrategy
from src.main.session import Session


class Robot(ABC):

    def __init__(self, session: Session, instruction_strategy: InstructionStrategy):
        self.__instructor = instruction_strategy
        self.__session = session

    def set_instruction_strategy(self, instruction_strategy):
        self.__instructor = instruction_strategy

    @abstractmethod
    def move(self, speed: float, time: float = None):
        """
        :param speed: Set movement speed in ...
        :param time: Set movement time in seconds
        """
        pass

    @abstractmethod
    def turn(self, degrees: int, wheel: Wheel):
        """
        :param degrees: Set how many degrees to turn
        :param wheel: Receive the opposite wheel to make the turn
        """
        pass

    @abstractmethod
    def turn_left(self, degrees: int):
        """
        :param degrees: Set how many degrees to turn to the left
        """
        pass

    @abstractmethod
    def turn_right(self, degrees: int):
        """
        :param degrees: Set how many degrees to turn to the right
        """
        pass

    @abstractmethod
    def stop(self):
        """
                        Stop the robot
        """
        pass
