import maya.cmds as cmds

# Make the body spheres
sphereBase = cmds.polySphere(radius=3)[0]
sphereMid = cmds.polySphere(radius=2)[0]
sphereTop = cmds.polySphere(radius=1.2)[0]
cmds.move(0, 3, 0, sphereBase, absolute=True)
cmds.move(0, 7, 0, sphereMid, absolute=True)
cmds.move(0, 9.5, 0, sphereTop, absolute=True)

# Make the eyes
eyeLeftCylinder = cmds.polyCylinder(radius=.25, height=.2)[0]
eyeRightCylinder = cmds.polyCylinder(radius=.25, height=.2)[0]
cmds.move(.7, 9.5, 1, eyeLeftCylinder, absolute=True)
cmds.move(-.7, 9.5, 1, eyeRightCylinder, absolute=True)
cmds.rotate(90, 30, 0, eyeLeftCylinder, relative=True, worldSpace=True)
cmds.rotate(90, -30, 0, eyeRightCylinder, relative=True, worldSpace=True)

# Make the hat
topHat = cmds.polyCylinder(radius=1.5, height=.2)[0]
cmds.move(0, 10, 0, topHat, absolute=True)
cmds.rotate(-10, 0, -5, topHat, relative=True, worldSpace=True)
cmds.select(topHat + ".f[21]")
cmds.polyExtrudeFacet(localScale=(0.75, 0.75, 0.75))
cmds.polyExtrudeFacet(localTranslateZ=2)

# Make the nose
noseCone = cmds.polyCone(radius=.25, height=1)[0]
cmds.move(0, 9.3, 1.5, noseCone, absolute=True)
cmds.rotate(90, 0, 0, noseCone, relative=True, worldSpace=True)

# Make the Arms
armLeftCylinder = cmds.polyCylinder(radius=.1, height=5)
cmds.move(-3, 6, 0, armLeftCylinder, absolute=True)
cmds.rotate(0, 0, -40, armLeftCylinder, relative=True, worldSpace=True)
armRightCylinder = cmds.polyCylinder(radius=.1, height=5)
cmds.move(3, 6, 0, armRightCylinder, absolute=True)
cmds.rotate(0, 0, 40, armRightCylinder, relative=True, worldSpace=True)

# Make the buttons
buttonCylinder = cmds.polyCylinder(radius=.25, height=.2)[0]
highButtonCylinder = cmds.polyCylinder(radius=.25, height=.25)[0]
cmds.move(0, 6.7, 2, buttonCylinder, absolute=True)
cmds.rotate(100, 0, 0, buttonCylinder, relative=True, worldSpace=True)
cmds.move(0, 8, 1.7, highButtonCylinder, absolute=True)
cmds.rotate(60, 0, 0, highButtonCylinder, relative=True, worldSpace=True)

# Make corncob pipe
pipeStraw = cmds.polyCylinder(radius=.05, height=1.3)[0]
pipeBucket = cmds.polyCylinder(radius=.15, height=.5)
cmds.move(.5, 8.9, 1.5, pipeStraw, absolute=True)
cmds.rotate(130, -10, 80, pipeStraw, relative=True, worldSpace=True)
cmds.move(.87, 8.9, 1.9, pipeBucket, absolute=True)
cmds.rotate(100, 90, 80, pipeBucket, relative=True, worldSpace=True)