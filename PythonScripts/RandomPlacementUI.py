import maya.cmds as cmds
import random


def placement_generator(x_min, x_max, y_min, y_max, z_min, z_max, num_dups):
    selected_objects = cmds.ls(selection=True) or []

    for obj in selected_objects:
        for _ in range(num_dups):
            duplicate_obj = cmds.duplicate(obj, rr=True)[0]

            rand_x = random.uniform(x_min, x_max)
            rand_y = random.uniform(y_min, y_max)
            rand_z = random.uniform(z_min, z_max)

            cmds.xform(duplicate_obj, worldSpace=True, translation=(rand_x, rand_y, rand_z))


def create_ui():
    window_name = "placementGeneratorUI"

    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name, window=True)

    cmds.window(window_name, title="Placement Generator UI", widthHeight=(300, 200))

    cmds.columnLayout(adjustableColumn=True)

    cmds.text(label="Set Range for X:")
    x_min_field = cmds.floatField(value=-10.0, precision=2, step=0.1, width=100, annotation="X Min")
    x_max_field = cmds.floatField(value=10.0, precision=2, step=0.1, width=100, annotation="X Max")

    cmds.text(label="Set Range for Y:")
    y_min_field = cmds.floatField(value=-20.0, precision=2, step=0.1, width=100, annotation="Y Min")
    y_max_field = cmds.floatField(value=40.0, precision=2, step=0.1, width=100, annotation="Y Max")

    cmds.text(label="Set Range for Z:")
    z_min_field = cmds.floatField(value=-10.0, precision=2, step=0.1, width=100, annotation="Z Min")
    z_max_field = cmds.floatField(value=10.0, precision=2, step=0.1, width=100, annotation="Z Max")

    cmds.text(label="Number of Duplicates:")
    num_dups_field = cmds.intField(value=5, minValue=1, width=200, annotation="Number of Duplicates")

    cmds.button(label="Generate Placement", command=lambda *args: generate_placement_callback(
        x_min_field, x_max_field, y_min_field, y_max_field, z_min_field, z_max_field, num_dups_field
    ))

    cmds.showWindow(window_name)


def generate_placement_callback(x_min_field, x_max_field, y_min_field, y_max_field, z_min_field, z_max_field,
                                num_dups_field):
    x_min = cmds.floatField(x_min_field, query=True, value=True)
    x_max = cmds.floatField(x_max_field, query=True, value=True)

    y_min = cmds.floatField(y_min_field, query=True, value=True)
    y_max = cmds.floatField(y_max_field, query=True, value=True)

    z_min = cmds.floatField(z_min_field, query=True, value=True)
    z_max = cmds.floatField(z_max_field, query=True, value=True)

    num_dups = cmds.intField(num_dups_field, query=True, value=True)

    placement_generator(x_min, x_max, y_min, y_max, z_min, z_max, num_dups)


# Create the UI
create_ui()
