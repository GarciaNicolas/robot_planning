from time import sleep

#from robot import Robot
from src.main.objects.wheel import Wheel
from src.main.objects.sensor import Sensor
from src.main.robot.instructionStrategy import InstructionStrategy
from src.main.session import Session


class Minipi():#Robot):

    def __init__(self, session: Session):#, instruction_strategy: InstructionStrategy):
        #super().__init__(session, instruction_strategy)
        self.__session = session
        self.__radius = 0.05601
        self.__left_wheel = Wheel(session.client_id, '/MiniPi/rueda_Izq')
        self.__right_wheel = Wheel(session.client_id, '/MiniPi/rueda_Der')
        # self.__ultrasonic = Ultrasonic()
        # self.__line_tracker = line_tracker

    def move(self, speed: float, time: float = None):
        self.__left_wheel.set_speed(speed)
        self.__right_wheel.set_speed(speed)

        if time:
            sleep(time)
            self.stop()

    def stop(self):
        self.__right_wheel.set_speed(0)
        self.__left_wheel.set_speed(0)

    def turn(self, degrees: int, wheel: Wheel):
        actual_speed = self.__right_wheel.get_speed()
        self.stop()
        turning_time = (degrees * self.__radius) / 5
        wheel.set_speed(5)
        sleep(turning_time)
        wheel.set_speed(0)
        self.move(actual_speed)

    def turn_right(self, degrees: int):
        self.turn(degrees, self.__left_wheel)

    def turn_left(self, degrees: int):
        self.turn(degrees, self.__right_wheel)
