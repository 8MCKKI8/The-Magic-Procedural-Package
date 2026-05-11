
__   __    _  __     
\ \ / /__ | |/ /___  
 \ V / _ \| ' // _ \ 
  | | (_) | . \ (_) |
  |_|\___/|_|\_\___/ 
---------------------
---------------------
HELLO! And Thank you for downloading YoKo.ORGANIC! 

Please paste the following into your Houdini Shelf tool!:


REMEMBER TO PUT YOUR REPLACE THE [********] WITH YOUR USERNAME!

AND PLEASE MOVE THE ACTUAL YOKO FILE (YoKo.version.0.0.0) TO YOUR DOWNLOADS FOLDER BEFORE CONTINUING!!!


THANK YOU!!!


-----------------------------------------------------------------------

import sys
import importlib

YOKO_ROOT = r"C:\Users\[********]\Downloads\YoKo.version 0.0.0"

if YOKO_ROOT not in sys.path:
    sys.path.insert(0, YOKO_ROOT)

import project
importlib.reload(project)


project.project()


-----------------------------------------------------------------------





