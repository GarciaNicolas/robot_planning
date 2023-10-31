from src.main.objects.object import Object
from src.utils import sim


class Wheel(Object):

    def __init__(self, client_id, name):
        super().__init__(client_id, name)
        self.speed = 0

    def set_speed(self, speed: float):
        self.speed = speed
        sim.simxSetJointTargetVelocity(self.__client_id, self.__handler, speed, sim.simx_opmode_streaming)

    def get_speed(self):
        return self.speed
