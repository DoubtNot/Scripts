import maya.cmds as cmds

def change_wireframe_color(color_index):
    # Get the selected objects
    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        cmds.warning("No objects selected. Please select at least one object.")
        return

    # Iterate through selected objects
    for obj in selected_objects:
        # Get the shape nodes of the selected object
        shape_nodes = cmds.listRelatives(obj, shapes=True) or []

        if not shape_nodes:
            cmds.warning(f"No shape nodes found for {obj}.")
            continue

        # Set the override color index for each shape node
        for shape_node in shape_nodes:
            cmds.setAttr(f"{shape_node}.overrideColor", color_index)

            # Ensure the override is turned on for the wireframe color
            cmds.setAttr(f"{shape_node}.overrideEnabled", 1)
            cmds.setAttr(f"{shape_node}.overrideRGBColors", 0)

# Example: Change wireframe color to index 13 (you can use any number between 0 and 31)
change_wireframe_color(13)
