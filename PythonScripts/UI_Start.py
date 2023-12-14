import maya.cmds as cmds

class CalculateUI():
    def__init__(self):

        self.window_name = 'Ricky'

    def delete(self):
        if cmds.window('%s The Calculator' % (self.window_name), exists = True):
            cmds.deleteUI('%s The Calculator' % (self.window_name))

    def create(self):
        self.delete()

        self.window_name = cmds.window(title = '%s The Calculator' % (self.window_name))


    cmds.columnLayout()

    cmds.button()
    cmds.button()
    cmds.button()
    cmds.button()

    cmds.showWindow(self.window_name)
