import maya.cmds as cmds

selection = cmds.ls(sl = True)

def sequenceNamer(name, objType):
    selection = cmds.ls(sl = True)

    if len(selection) > 999:
        numberPadding = 4
    elif len(selection) > 99:
        numberPadding = 3
    elif len(selection) > 9:
        numberPadding = 2
    else: numberPadding = 1

    for count, object in enumerate(selection):
        cmds.rename(object, name + "_" + str(count + 1).zfill(numberPadding) + "_" + objType)

sequenceNamer("Leg", "Jnt")

