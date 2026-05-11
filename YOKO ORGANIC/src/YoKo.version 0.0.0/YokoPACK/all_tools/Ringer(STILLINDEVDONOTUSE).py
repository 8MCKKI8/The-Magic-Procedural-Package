import hou  # type: ignore

def Tool_Two_Organic_Ringer():

    obj = hou.node('/obj')

    
    geo = obj.createNode('geo', 'YOKO_organic_ringer')

    



    thelinebackbone = geo.createNode ('line','line_backbone')

    thelinebackbone.parm("length").set(4)
    thelinebackbone.parm("points").set(10)

    thelinebackbone.parm("dirx").set(0)
    thelinebackbone.parm("diry").set(0)
    thelinebackbone.parm("dirz").set(1)
        
    sweepOne = geo.createNode('sweep', 'sweep1')

    bendOne = geo.createNode('bend', 'bend2')


    bendOne.parm("capturelength").set(4)

    bendOne.parm("directionz").set(1) 
    bendOne.parm("directiony").set(0)

    bendOne.parm("curveu").set(.5)

    groupOne = geo.createNode('group','group1')

    converter = geo.createNode('convert','convert1')

    attributeMain = geo.createNode('attribnoise', 'attribunoise1')

    smoother = geo.createNode('smooth','smooth1')

    editnumberOne = geo.createNode('edit', 'edit1')

    transformer = geo.createNode('transform','transform1')

# remember to add all of this after your node creation: 

    

    sweepOne.setInput(0, thelinebackbone)
   


    
    
    bendOne.setInput(0, sweepOne)

    groupOne.setInput(0, bendOne)

    converter.setInput(0, groupOne)

    attributeMain.setInput(0, converter)

    smoother.setInput(0, attributeMain)

    editnumberOne.setInput(0, smoother)

    transformer.setInput(0, editnumberOne)



    transformer.setDisplayFlag(True)
    transformer.setRenderFlag(True)
        

    
    geo.layoutChildren()
   
   
Tool_Two_Organic_Ringer()




