from maya import cmds

def createPrimitive(name):
	if name == "cube":
		cmds.polyCube(name="Cube")
	elif name == "sphere":
		cmds.polySphere(name="Sphere")
	elif name == "cone":
		cmds.polyCone(name="Cone")
	elif name == "torus":
		cmds.polyTorus(name="Torus")
	else:
		cmds.warning(f"Unknown primitive: {name}")

