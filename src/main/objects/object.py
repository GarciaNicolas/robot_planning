from src.utils import sim


class Object:

    def __init__(self, client_id: int, name: str):
        self.__handler = sim.simxGetObjectHandle(client_id, name, sim.simx_opmode_blocking)
        self.__client_id = client_id
        if self.__handler != sim.simx_return_ok:
            raise Exception(f"Fail getting handler of {name}")
