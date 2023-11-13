import maya.cmds as cmds

def change_wireframe_color(color_index):

    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        cmds.warning("No objects selected. Please select at least one object.")
        return

    for obj in selected_objects:
        shape_nodes = cmds.listRelatives(obj, shapes=True) or []

        if not shape_nodes:
            cmds.warning(f"No shape nodes found for {obj}.")
            continue

        for shape_node in shape_nodes:
            cmds.setAttr(f"{shape_node}.overrideColor", color_index)

            cmds.setAttr(f"{shape_node}.overrideEnabled", 1)
            cmds.setAttr(f"{shape_node}.overrideRGBColors", 0)

# How To Use: Change wireframe color to a new color (you can use any number between 0 and 31)
change_wireframe_color(13)
