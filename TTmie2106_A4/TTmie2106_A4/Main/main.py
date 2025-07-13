from Application.VectorController import VectorRepositoryController
from Infrastructure.VectorRepository import VectorRepository
from UI.UI import VectorUI

def start():
    vector_repo = VectorRepository([])          #create a empty repository
    vector_controller = VectorRepositoryController(vector_repo)         #create the controller which calls the repository
    vector_ui = VectorUI(vector_controller)         #create the ui which calls the controller
    vector_ui.main_meniu()  #call the main meniu

if __name__ == '__main__':      #start the app
    start()