# THE MAGIC PROCEDURAL PACKAGE: YoKo

## Demo
Demo Video: <https://youtu.be/-S2yAn5NEzA?si=I4fi3N28Ohlrdizx>

## GitHub Repository
GitHub Repo: <https://github.com/8MCKKI8/The-Magic-Procedural-Package.git>

## # YOKO ORGANIC

YOKO ORGANIC is a custom procedural toolset created for Houdini that focuses on making procedural world building more accessible and beginner friendly.
The project was designed to simplify the process of developing geo node setups by generating customizable built-in geometry systems automatically with the click of a button. 
Instead of requiring users to manually create every node network from scratch, the toolset helps automate repetitive setup tasks while still allowing artists to customize and expand the generated networks.
The overall goal of the project is to help newer users become more comfortable with Houdini’s procedural workflow (even when it can be intimidating at first), and also speed up productivity for experienced users.

The repository contains several files that work together to create the complete package.
 The main Python logic is located inside the src/project.py file, which handles the creation of geometry nodes, interface behavior, and procedural setup automation. 
 Additional scripts are used to organize the custom tools and connect them to the user interface. To set up, users must create a new shelf and create a tool. 
 They then will have to copy and paste the provided code into the new tool script.
  Other folders in the repository contain icons, UI resources, and package configuration files that allow the toolset to work on all computers.

One of the biggest design considerations during development was usability. Houdini is an extremely powerful software package, but it can be very hard to work with, especially for new users. 
Because of this, the project was designed to be as easy as possible. The UI and procedural systems were created to reduce unnecessary complexity while still exposing users to procedural concepts such as node connections, geometry generation, and parameter customization.
 Another major challenge was portability. I had a bit of trouble with packaging, but I managed to get it to work for all devices. The only aspect is that users must enter their username and put the file in downloads.

There are many future improvements that I would love to expand upon. 
Due to timing, unfortunately two buttons weren’t able to work (but they will be developed really soon). 
Instead, as a placeholder, a message is displayed (for professionalism). I would also love to develop more buttons that not only work in OBJ mode but in stage mode and LOPs as well.
 (I really want to expand with texturing and lighting.) I loved this whole process, and the fact I was able to create it and build upon it really makes me happy.

Overall, YOKO ORGANIC serves as both a procedural utility package and a learning tool that encourages users to explore proceduralism in a fun and educational way.