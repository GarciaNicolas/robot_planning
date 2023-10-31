from time import sleep

from src.utils import sim


class Session:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, ip, port):
        self.client_id = sim.simxStart(ip, port, True, True, 5000, 1)
        if self.client_id != sim.simx_return_ok:
            raise Exception('Unable to connect to simulator.')
        sim.simxAddStatusbarMessage(self.client_id, 'User connected.', sim.simx_opmode_oneshot)
        print("Connected to the simulator.")

    @staticmethod
    def close():
        sim.simxAddStatusbarMessage(Session._instance.client_id, 'User disconnecting.', sim.simx_opmode_oneshot)
        sleep(0.1)
        print("Disconnecting from the simulator.")
        sim.simxFinish(-1)
        Session._instance = None
