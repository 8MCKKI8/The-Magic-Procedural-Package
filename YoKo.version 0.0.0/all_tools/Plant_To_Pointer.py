import hou

def run():

    
    obj = hou.node('/obj') # type: ignore

    existing = obj.node('YOKO_PlantToPoint')
    if existing:
        existing.destroy()

    geo = obj.createNode('geo','YOKO_PlantToPoint')

    grid = geo.createNode('grid','grid1')
    grid.parm("rows").set(10)
    grid.parm("cols").set(10)

    scatter = geo.createNode('scatter::2.0','scatter1')
    copytopoints = geo.createNode('copytopoints::2.0', 'copytopoints1')
    objectmerge = geo.createNode('object_merge','objectmerge1')


    copytopoints.setInput(1, scatter)  
    scatter.setInput(0, grid) 
    copytopoints.setInput(0, objectmerge) 

    #THIS IS HIGHLY IMPORTANT IT LAYOUTS EVERYTHING ITS NOT JUST FOR SHOW!!!
    geo.layoutChildren()
    


