from Application.PlaneController import PlaneController
from Infrastructure.PlaneRepository import PlaneRepository
from UI.PlaneUI import PlaneUI

def start():
    repo=PlaneRepository([])
    controller=PlaneController(repo)
    plane_ui=PlaneUI(controller)
    plane_ui.main_meniu()

if __name__ == '__main__':
    start()