import maya.cmds as cmds


def changeColor(control, color):
    cmds.setAttr(control + ".overrideEnabled", 1)
    cmds.setAttr(control + ".overrideColor", color)

def createControl(index):
    selection = cmds.ls(sl=True)
    for count, object in enumerate(selection):
        name = object.rpartition("_")
        if name[0] == "":
            control = cmds.circle(n=name[2] + "_Ctrl")
        else:
            control = cmds.circle(n=name[0] + "_Ctrl")
        changeColor(control[0], index)
        cmds.matchTransform(control, object)
        dup = cmds.group(n=control[0] + "_Grp")

createControl(13)






    #for each selection, create nurbs circle, give nurbs circle selections name with _Ctrl suffix, deleting previous suffix, match transformations of selection, duplicate, freeze, and parent first nurbs into duplicate.


