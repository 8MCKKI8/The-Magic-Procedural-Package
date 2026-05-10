import sys
import os
import hou



def get_project_root():
    folder_name = "YoKo.version 0.0.0"

    try:
        path = os.path.abspath(__file__)
    except:
        path = os.getcwd()

    while True:
        if os.path.basename(path) == folder_name:
            return path

        parent = os.path.dirname(path)
        if parent == path:
            break
        path = parent

    hip = hou.getenv("HIP")
    if hip:
        hip_dir = os.path.dirname(hip)

        while True:
            if os.path.basename(hip_dir) == folder_name:
                return hip_dir

            parent = os.path.dirname(hip_dir)
            if parent == hip_dir:
                break
            hip_dir = parent

    return os.getcwd()


PROJECT_ROOT = get_project_root()


from PySide6 import QtWidgets, QtUiTools, QtCore, QtGui


from all_tools.Aqua_Warp import run as aqua_warp
from all_tools.Dotter import run as dotter
from all_tools.Plant_To_Pointer import run as pointer
from all_tools.Poly_Warp import run as polywarp
from all_tools.Toon_To_Mod import run as toontomod



class YokoUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        loader = QtUiTools.QUiLoader()

       
        ui_path = os.path.join(
            PROJECT_ROOT,
            "Downloads",
            "YoKo.version 0.0.0",
            "YokoPACK",
            "yoko.ui"
        )

        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")

        ui_file = QtCore.QFile(ui_path)

        if not ui_file.open(QtCore.QFile.ReadOnly):
            raise RuntimeError(f"Cannot open UI file: {ui_path}")

        self.ui = loader.load(ui_file, self)
        ui_file.close()

        if self.ui is None:
            raise RuntimeError(f"Failed to load UI: {ui_path}")

        #Qt
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.ui)

        #Icons
        ICON_ROOT = r"C:\Users\Micki\Downloads\YoKo.version 0.0.0\icons"

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

        icon_paths = [
            os.path.join(ICON_ROOT, i)
            for i in icons
        ]

        names = [
            "AguaWarp",
            "Guide",
            "Morpher",
            "Plane",
            "PlantToPoint",
            "Pointer",
            "Ringer",
            "ImageToMod"
        ]

        self.actions = [
            aqua_warp,
            dotter,
            polywarp,
            None,
            pointer,
            None,
            None,
            toontomod
        ]

        #J.I.C
        def safe_call(func):
            def wrapper():
                try:
                    func()
                except Exception as e:
                    hou.ui.displayMessage(str(e))
            return wrapper

       #UI design
        for i in range(len(names)):

            btn = QtWidgets.QPushButton(names[i])

            # icon
            if os.path.exists(icon_paths[i]):
                btn.setIcon(QtGui.QIcon(icon_paths[i]))

            btn.setIconSize(QtCore.QSize(100, 100))

            action = self.actions[i]

            if action:
                btn.clicked.connect(safe_call(action))

            layout.addWidget(btn)


#Display
window = YokoUI()
hou.session.yoko_window = window
window.show()