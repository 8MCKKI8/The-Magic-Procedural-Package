
__   __    _  __     
\ \ / /__ | |/ /___  
 \ V / _ \| ' // _ \ 
  | | (_) | . \ (_) |
  |_|\___/|_|\_\___/ 
---------------------
---------------------
HELLO! And Thank you for downloading YoKo.ORGANIC! 

The following are  the steps on how to properly  set it up!

1.Move the actual YoKo file: (YoKo.version.0.0.0) to your downloads folder. (this is a requirement)

----------------------------------------------

2. Create a new self with a new shelf tool in Houdini.

(if you're having trouble with this please watch this tutorial: https://youtu.be/Iv2EfRohc7o?si=02yT7WQVvAL145dj)

-------------------------------------------------

3. Please paste the following into your Houdini Shelf tool!:


REMEMBER TO PUT YOUR REPLACE THE [********] WITH YOUR DESKTOP USERNAME!


  ____          _      
 / ___|___   __| | ___ 
| |   / _ \ / _` |/ _ \
| |__| (_) | (_)| |  __/
 \____\___/ \__,_|\___|
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





enjoy!