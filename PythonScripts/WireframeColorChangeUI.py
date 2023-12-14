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

def show_ui():
    window_name = "changeWireframeColorUI"

    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name, window=True)

    cmds.window(window_name, title="Change Wireframe Color", widthHeight=(300, 120))
    cmds.columnLayout(adjustableColumn=True)

    cmds.text(label="Enter a number between 0 and 31:", align="left", font="boldLabelFont")
    color_index_field = cmds.intField(minValue=0, maxValue=31, value=13, width=200, annotation="Enter color index (0-31):")
    cmds.button(label="Change Color", command=lambda x: change_wireframe_color(cmds.intField(color_index_field, query=True, value=True)))

    cmds.showWindow(window_name)

# To use the UI, call the show_ui function
show_ui()
