from controllers import RegistrationSystem
from ui.main_gui import MainGUI
from seed_courses import seed_courses

def main():
    system = RegistrationSystem()
    seed_courses(system)
    
    gui = MainGUI(system)
    gui.run()

if __name__ == "__main__":
    main()