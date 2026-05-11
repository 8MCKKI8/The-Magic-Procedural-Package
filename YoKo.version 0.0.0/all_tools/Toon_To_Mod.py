import hou  # type: ignore

def run():

    obj = hou.node('/obj')

    
    geo = obj.createNode('geo', 'YOKO_toon_toMod')

   
    trace_node = geo.createNode('trace', 'trace1')
    polyextrude = geo.createNode('polyextrude', 'polyextrude1')

    
    polyextrude.setInput(0, trace_node)

    
    alterator = geo.createNode('null', 'YOKO_Alterator')
    alterator.setInput(0, polyextrude)

   
    geo.layoutChildren()

    
    parm_group = alterator.parmTemplateGroup()

    parameter = hou.FloatParmTemplate(
        "alterator",
        "expand",
        1
    )

    parm_group.append(parameter)
    alterator.setParmTemplateGroup(parm_group)

    polyextrude.parm('/obj/YOKO_toon_toMod/polyextrude1/dist').setExpression(
    'ch("/obj/YOKO_toon_toMod/YOKO_Alterator/alterator")',
    language=hou.exprLanguage.Hscript
)




def Tool_Two_PolyWARP():
    sphere = geo.createNode('sphere', 'YOKO_poly')
    resampler = geo.createNode('resample1', 'polyextrude1')