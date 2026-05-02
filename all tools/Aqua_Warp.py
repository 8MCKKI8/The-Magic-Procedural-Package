def Tool_Four_AguaWarp():

    obj = hou.node('/obj')

    existing = obj.node('YOKO_agua_warp')
    if existing:
        existing.destroy()

    geo = obj.createNode('geo', 'YOKO_aqua_warp')

    grid = geo.createNode('grid', 'grid1')
    grid.parm("rows").set(100)
    grid.parm("cols").set(100)

    noise = geo.createNode('attribnoise', 'attribnoise1')
    noise.parm("attribs").set("P")

    smoother = geo.createNode('smooth', 'smooth1')
    oceanEval = geo.createNode('oceanevaluate', 'oceanevaluate1')
    oceanSpectrum = geo.createNode('oceanspectrum', 'oceanspectrum1')

    alterator = geo.createNode('null', 'YOKO_Alterator')

    parm_group = alterator.parmTemplateGroup()

    parameter = hou.FloatParmTemplate(
        "element_size",
        "wave_size",
        1,
        default_value=(1.0,)
    )


    parameter = hou.FloatParmTemplate(
        "element_size",
        "wave_shaper",
        1,
        default_value=(1.0,)
    )
    
    parm_group.addParmTemplate(parameter)
    alterator.setParmTemplateGroup(parm_group)

  
    noise.parm("elementsize").setExpression(
        'ch("../YOKO_Alterator/element_size")'
    )


    noise.setInput(0, grid)
    smoother.setInput(0, noise)
    oceanEval.setInput(0, smoother)

    oceanEval.setInput(1, oceanSpectrum)
   

    geo.layoutChildren()

Tool_Four_AguaWarp()

#NEED TO FINISH: MUST ADD A SECOND PARAMETER FOR THE GRADIENT WARP PARAMETER AND CONNECT IT. 