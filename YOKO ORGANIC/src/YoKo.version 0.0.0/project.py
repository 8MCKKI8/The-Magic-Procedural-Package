import os
import sys

PROJECT_ROOT = os.environ.get("YOKO_ROOT")

if not PROJECT_ROOT:
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.abspath(PROJECT_ROOT)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)



from PySide6 import QtWidgets, QtUiTools, QtCore, QtGui

from all_tools.Aqua_Warp import run as aqua_warp
from all_tools.Guide import run as guide
from all_tools.Plane import run as plane
from all_tools.Dotter import run as dotter
from all_tools.Plant_To_Pointer import run as pointer
from all_tools.Poly_Warp import run as polywarp
from all_tools.Toon_To_Mod import run as toontomod
from all_tools.Ringer_Message import run as message




class main(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

    

        loader = QtUiTools.QUiLoader()

        ui_path = os.path.join(PROJECT_ROOT, "UI_Setup", "yoko.ui")

        if not os.path.exists(ui_path):
            raise FileNotFoundError(ui_path)

        ui_file = QtCore.QFile(ui_path)
        ui_file.open(QtCore.QFile.ReadOnly)

        self.ui = loader.load(ui_file, self)
        ui_file.close()

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.ui)

        
        ICON_ROOT = os.path.join(PROJECT_ROOT, "icons")

        icons = [
            "AguaWarp.icon.png",
            "Ryyuko.icon.png",
            "Morph.icon.png",
            "Plane.icon.png",
            "Plant.icon.png",
            "Point.icon.png",
            "Ringer.icon.png",
            "Image.icon.png",
        ]

        icon_paths = [os.path.join(ICON_ROOT, i) for i in icons]

        names = [
            "AguaWarp",
            "Guide",
            "Morpher",
            "Plane",
            "PlantToPoint",
            "Dotter",
            "Ringer",
            "ImageToMod"
        ]

        self.actions = [
            aqua_warp,
            guide,
            polywarp,
            message,
            pointer,
            dotter,
            message,
            toontomod
        ]

        def safe_call(name, func):
            def wrapper():
                
                try:
                    func()
                except Exception as e:
                    hou.ui.displayMessage(str(e))
            return wrapper

        for i in range(len(names)):

            name = names[i]
            action = self.actions[i]

            btn = QtWidgets.QPushButton(name)

            if os.path.exists(icon_paths[i]):
                btn.setIcon(QtGui.QIcon(icon_paths[i]))

            btn.setIconSize(QtCore.QSize(64, 64))

            if action:
                btn.clicked.connect(safe_call(name, action))

            layout.addWidget(btn)



def project():
    
    window = main()
    hou.session.main_window = window
    window.show()
