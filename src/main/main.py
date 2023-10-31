from src.main.session import Session
from src.main.robot.minipi import Minipi
from src.utils import sim

if __name__ == '__main__':

    #session = Session(ip, port)
    minipi = Minipi(session)
    minipi.move(5,2)

    session.close()
