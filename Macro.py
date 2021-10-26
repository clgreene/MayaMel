import maya.cmds as cmds

object[]


cmds.polyCube(axis =[0, 1, 0],
              createUVs = 2,
              constructionHistory = 1,
              depth = 5,
              height = 5,
              width = 5,
              name = 'DieBody'
              )
cmds.move(0, 2.5, 0)

cmds.polyBevel(constructionHistory = 1,
               offset = .35,
               segments = 3,
               )

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot01'
                )

cmds.scale(.5, .15, .5)

cmds.move(0, 5, 0)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot02'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(90, 0, 0)

cmds.move(1, 3.5, 2.5)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot03'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(90, 0, 0)

cmds.move(-1, 1.5, 2.5)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot04'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(0, 0, 90)

cmds.move(2.5, 2.5, 0)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot05'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(0, 0, 90)

cmds.move(2.5, 3.75, 1.25)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot06'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(0, 0, 90)

cmds.move(2.5, 1.25, -1.25)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot07'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(0, 0, 90)

cmds.move(-2.5, 1.25, -1.25)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot08'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(0, 0, 90)

cmds.move(-2.5, 1.25, 1.25)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot09'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(0, 0, 90)

cmds.move(-2.5, 3.75, 1.25)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot10'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(0, 0, 90)

cmds.move(-2.5, 3.75, -1.25)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot11'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(90, 0, 0)

cmds.move(-1.25, 1.25, -2.5)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot12'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(90, 0, 0)

cmds.move(-1.25, 3.75, -2.5)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot13'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(90, 0, 0)

cmds.move(1.25, 3.75, -2.5)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot14'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(90, 0, 0)

cmds.move(1.25, 1.25, -2.5)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot15'
                )

cmds.scale(.5, .15, .5)

cmds.rotate(90, 0, 0)

cmds.move(0, 2.5, -2.5)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot16'
                )

cmds.scale(.5, .15, .5)

cmds.move(1.25, 0, -1.25)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot17'
                )

cmds.scale(.5, .15, .5)

cmds.move(1.25, 0, 0)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot18'
                )

cmds.scale(.5, .15, .5)

cmds.move(1.25, 0, 1.25)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot19'
                )

cmds.scale(.5, .15, .5)

cmds.move(-1.25, 0, -1.25)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot20'
                )

cmds.scale(.5, .15, .5)

cmds.move(-1.25, 0, 0)

cmds.polySphere(axis = [0,1,0],
                createUVs = 2,
                constructionHistory = 1,
                name = 'Dot21'
                )

cmds.scale(.5, .15, .5)

cmds.move(-1.25, 0, 1.25)




