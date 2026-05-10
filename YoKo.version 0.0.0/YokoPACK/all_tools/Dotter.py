

def run():

    obj = hou.node('/obj') # type: ignore

    existing = obj.node('YOKO dotter')
    if existing:
        existing.destroy()

    geo = obj.createNode('geo','YOKO_dotter')

    alterator = geo.createNode('null', 'YOKO_Alterator')


    parm_group = alterator.parmTemplateGroup()

    parameter = hou.FloatParmTemplate(
        "element_size",
        "position and align",
        1,
        default_value=(1.0,)
    )


    parameter = hou.FloatParmTemplate(
        "element_size",
        "position and align",
        1,
        default_value=(1.0,)
    )
    
    parm_group.addParmTemplate(parameter)
    alterator.setParmTemplateGroup(parm_group)

    sphere = geo.createNode('sphere', 'YOKO_particle_default')
    #REMEMBER TO CONVERT A SPHERE TO A POLYGON MESH YOU MUST USE THIS ---->
    sphere.parm("type").set(1)

    sphere.parm("freq").set(6)


    grid = geo.createNode('grid','default_grid')
    grid.parm("rows").set(5)
    grid.parm("cols").set(5)

    scatter = geo.createNode('scatter::2.0','scatter1')
    
    transform = geo.createNode('xform','transform1')
    transform.parm("scale").setExpression(
        'ch("../YOKO_Alterator/element_size")'
    )


    copytopoints = geo.createNode('copytopoints::2.0', 'copytopoints1')




    # REMEMBER TO ALWAYS WIRE THEM WITH THIS
     
    copytopoints.setInput(1,transform)

    scatter.setInput(0, grid)
    
    # IMPORTANT PART
    copytopoints.setInput(0, sphere)   # sphere = source geometry
    copytopoints.setInput(1, scatter)  # scatter = points
    transform.setInput(0,grid)
    copytopoints.setInput(1, transform)  # scatter = points

    copytopoints.setDisplayFlag(True)
    copytopoints.setRenderFlag(True)


    geo.layoutChildren()




#LIFESAVER: TELLS THE NAMES OF THE NODES
#import hou

#nodes = hou.selectedNodes()
#if nodes:
    #print(nodes[0].type().name())
#else:
    #print("No node selected")
    


    




