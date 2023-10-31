from abc import ABC, abstractmethod


class InstructionStrategy(ABC):

    @abstractmethod
    def follow_instructions(self):
        pass

class ListedStrategy(InstructionStrategy):

    def follow_instructions(self):
        os.read(path)

