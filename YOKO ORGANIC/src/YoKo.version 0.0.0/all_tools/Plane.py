import hou  # type: ignore

def run():

    obj = hou.node('/obj')

    geo = obj.createNode('geo', 'YOKO_Plane')

   
    grid = geo.createNode('grid', 'grid1')
    polyextrude = geo.createNode('polyextrude', 'polyextrude1')
    output = geo.createNode('null', 'YOKO_Alterator')

   
    polyextrude.setInput(0, grid)
    output.setInput(0, polyextrude)

    
    parm_group = geo.parmTemplateGroup()

    dist_parm = hou.FloatParmTemplate(
        "dist",
        "Distance",
        1,
        default_value=(0.1,)
    )

    parm_group.append(dist_parm)
    geo.setParmTemplateGroup(parm_group)


    polyextrude.parm("distance").setExpression('ch("../dist")', hou.exprLanguage.Hscript)

    
    geo.layoutChildren()

    #THIS CODE IS STILL IN DEV DO NOT USE!!!!!!!!!