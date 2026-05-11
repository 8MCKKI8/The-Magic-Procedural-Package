import hou  # type: ignore

def run():

    obj = hou.node('/obj')

    existing = obj.node('YOKO_poly_warp')
    if existing:
        existing.destroy()

    geo = obj.createNode('geo', 'YOKO_poly_warp')

    polygonSphere = geo.createNode('sphere', 'sphere1')
    polygonSphere.parm("type").set(2)  # polygon mesh
    polygonSphere.parm("scale").set(0.5)
    polygonSphere.parm("rows").set(24)
    polygonSphere.parm("cols").set(24)

    resampler = geo.createNode('resample', 'resample1')
    resampler.parm("group").set("pointer")

    attribute = geo.createNode('attribrandomize', 'attribrandomize1')
    attribute.parm("name").set("Cd")

    noise = geo.createNode('attribnoise', 'attribnoise1')
    noise.parm("attribs").set("P")
    noise.parm("amplitude").set(3.26)

    smoother = geo.createNode('smooth', 'smooth1')
    smootherTwo = geo.createNode('smooth', 'smooth2')

    resampler.setInput(0, polygonSphere)
    attribute.setInput(0, resampler)
    noise.setInput(0, attribute)
    smoother.setInput(0, noise)
    smootherTwo.setInput(0, smoother)

    smootherTwo.setDisplayFlag(True)
    smootherTwo.setRenderFlag(True)

   
    alterator = geo.createNode('null', 'YOKO_Alterator')

  
    parm_group = alterator.parmTemplateGroup()

    parameter = hou.FloatParmTemplate(
        "element_size",
        "Element Size",
        1,
        default_value=(1.0,)
    )

    parm_group.addParmTemplate(parameter)
    alterator.setParmTemplateGroup(parm_group)

  
    noise.parm("elementsize").setExpression(
        'ch("../YOKO_Alterator/element_size")'
    )

    

